<<<<<<< HEAD
while true
do
    response=$(curl -o -I -L --write-out %{http_code} http://34.70.194.178:8080/lazy)
echo "\nResponseCoder..."$response
echo "\nDone ...\n\n"
sleep 1
=======
while true
do
    response=$(curl -o -I -L --write-out %{http_code} http://34.70.194.178:8080/lazy)
echo "\nResponseCoder..."$response
echo "\nDone ...\n\n"
sleep 1
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
done