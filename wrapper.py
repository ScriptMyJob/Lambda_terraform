#!/usr/bin/env python
# Written by:   Robert J.
#               Robert@scriptmyjob.com

import subprocess

#######################################
### Main Function #####################
#######################################

def main():
    try:
        out = subprocess.check_output(
            ["Resources/terraform", "apply", "Terraform/"]
        )
    except OSError:
        out = subprocess.check_output(
            ["terraform", "apply", "Terraform/"]
        )

    print out

    return out


#######################################
### Execution #########################
#######################################

if __name__ == "__main__":
    main()


def execute_me_lambda(event, context):
    out = main()
    return out
