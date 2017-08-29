#!/usr/bin/env python
# Written by:   Robert J.
#               Robert@scriptmyjob.com

import subprocess

#######################################
### Main Function #####################
#######################################

def main():
    subprocess.call(
        ["Resources/terraform", "apply", "Terraform/"]
    )


#######################################
### Execution #########################
#######################################

if __name__ == "__main__":
    main()


def execute_me_lambda(event, context):
    out = main()
    return out
