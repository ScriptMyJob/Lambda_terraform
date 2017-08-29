terraform {
    backend "s3" {
        bucket  = "scriptmyjob.terraform.tfstate"
        key     = "terraform.tfstate"
        region  = "us-west-2"
    }
}
