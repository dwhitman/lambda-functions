import boto3

def lambda_handler(event, context): 
    rds_dbs = ['plantronicsmanager', 'plantronicsmanager-ap', 'plantronicsmanager-au', 'plantronicsmanager-eu', 'pltsystem']
    #rds_dbs = ['plantronicsmanager-ap']

    for db in rds_dbs:
    
        rds_client = boto3.client('rds')
    
        db_status = rds_client.describe_db_instances(DBInstanceIdentifier=db)
        print ("RDS " + db + " is: " + db_status['DBInstances'][0]['DBInstanceStatus'])
    
        if 'stopped' in db_status['DBInstances'][0]['DBInstanceStatus']:
            print ("- starting " + db)
            rds_client.start_db_instance(DBInstanceIdentifier=db)
        

lambda_handler(1,2)
