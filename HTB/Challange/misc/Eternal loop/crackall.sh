#echo "creating numeric list"
#crunch 1 6 1234567890 -o num.list &>> /dev/null

echo "run fcrackzip"
while [[ true ]]; do 
	file = $(ls | grep zip)
	fcrackzip -u -D -p num.list $file > result
	pass = $(cat result | tr -d '\n' | awk '{print $5}')
	result = $(cat result | tr -d '\n' | grep FOUND)
	echo $result
	if [[ -z $result ]]; then
		echo "No Password Found in file $file" 
		break 2
	else
		echo "Password Found in file $file = $pass"
		unzip -q -P "$pass" "$(ls | grep zip)"
		rm $file
	fi
done


