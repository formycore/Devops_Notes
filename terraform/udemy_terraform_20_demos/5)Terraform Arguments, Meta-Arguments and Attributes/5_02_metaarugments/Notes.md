# for_each loop
- lets take the region for the us-east-1, has 6 AZs
- if we want to create the 6 instances on each AZS, we can use the for_each loop
- we need to get the list of availabitlity zones
- no need for local zones only on the availability zones
- add the below code to c5-ec2instance.tf
```
################################

data "aws_availability_zones" "my_azones" {
  filter {
    name   = "opt-in-status"
    values = ["opt-in-not-required"]
  }
}
################################
```
# for_each 
- for_each is a meta-argument that accepts a map or a set of strings
- equivalent to count, but only accepts maps and sets, not numbers
- count only gives the count.index
- for_each we can provide the subnet id,availability zone id, etc
- FOR_EACH IS USED TO CREATE MULTIPLE INSTANCES OF THAT RESOURCE
- for_each [ "us-east-1", "us-east-2 ] it wont accept this as it is a list
- for_each = [ "data.aws_availability_zones.my_azones.names" ]

# toset
- toset() function converts a list into a set
- toset ["a", "b", 3] = {"a", "b", "3"}
- transform element into a same type, mixed elements converted into most general type
- also removes the duplicates
- toset(["a","a","b"]) = {"a", "b"}
- for set of strings, each.key and each.value are the same
- toset(data.aws_availability_zones.my_azones.names) # this will convert the list into a set
