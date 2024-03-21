#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { S3BucketStackStack } from '../lib/s3_bucket_stack-stack';

const app = new cdk.App();
new S3BucketStackStack(app, 'S3BucketStackStack');
