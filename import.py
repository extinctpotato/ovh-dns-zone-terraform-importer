import sys, hcl, ovh, os

# Define constants.
OVH_TF_RESOURCE = "ovh_domain_zone_record"

# Parse args.
creds_tf = sys.argv[1]
zone = sys.argv[2]
main_tf = 'main.tf'
import_sh = 'import.sh'

try:
    main_tf = sys.argv[3]
    import_sh = sys.argv[4]
except IndexError:
    pass

main_tf_contents = ''
import_sh_contents = ''

# Create TF-friendly zone prefix.
zone_res_name = zone.replace(".", "_dot_")

# Load OVH credentials.
with open(creds_tf, 'r') as f:
    creds_hcl = hcl.load(f)

ovh_client = ovh.Client(**creds_hcl['provider']['ovh'])

record_ids = ovh_client.get(f'/domain/zone/{zone}/record')

for r_id in record_ids:
    record = ovh_client.get(f'/domain/zone/{zone}/record/{r_id}')

    terraform_resource_name = f"{zone_res_name}_{r_id}"

    main_tf_contents += (f'resource "{OVH_TF_RESOURCE}" "{terraform_resource_name}" ' + '{\n')

    for k,v in record.items():
        # Resource ID is not part of the configuration.
        if v == 'id':
            continue

        # Record values might contain double quotes.
        v_escaped = str(v).replace('"', r'\"')
        main_tf_contents += f'    {k.lower()} = "{v_escaped}"\n'

    main_tf_contents += '}\n\n'

with open(main_tf, 'w') as f:
    f.write(main_tf_contents)
