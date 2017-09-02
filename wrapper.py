#!/usr/bin/env python
# Written by:   Robert J.
#               Robert@scriptmyjob.com

import subprocess
import sys

#######################################
### Main Function #####################
#######################################

def main():
    try:
        out = subprocess.check_output(
            ["Resources/terraform", "init", "Terraform/"]
        )
    except OSError:
        out = subprocess.check_output(
            ["terraform", "init", "Terraform/"]
        )
    except subprocess.CalledProcessError, e:
        print e.output
        sys.exit()

    print out

    try:
        out = subprocess.check_output(
            ["Resources/terraform", "apply", "Terraform/"]
        )
    except OSError:
        out = subprocess.check_output(
            ["terraform", "apply", "Terraform/"]
        )
    except subprocess.CalledProcessError, e:
        print e.output
        sys.exit()

    print out

    return out


#######################################
### Execution #########################
#######################################

if __name__ == "__main__":
    main()


def execute_me_lambda(event, context):
    result = main()
    return result
