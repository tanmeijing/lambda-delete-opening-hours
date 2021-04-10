terraform {
  backend "s3" {
    bucket = "nus-iss-equeue-terraform"
    key    = "lambda/delete-opening-hours/tfstate"
    region = "us-east-1"
  }
}