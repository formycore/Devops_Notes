# output for loop with list
output "for_output_list" {
  value = [for instance in aws_instance.myec2vm: instance.public_ip]
  /*
  in the c5-ec2instances.tf file, we have created 2 ec2 instances.
  as the count=2

  */
}
# output for loop with map
output "for_output_map" {
  value = {for instance in aws_instance.myec2vm: instance.id => instance.public_ip}
  /*
  

  */
}

# output for loop with map advanced
output "for_output_map2" {
    value = {for c, instance in aws_instance.myec2vm: c => instance.public_dns}
        /*
        if the count is 0 then the output will be
        {
            "0" = {
                "0" = "ec2-3-xx8-135-163.compute-1.amazonaws.com"
            }
        }
        */
    }
# output with splat operator 
