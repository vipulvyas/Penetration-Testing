while [ "`find . -type f -name '*.zip' | wc -l`" -gt 0 ]
do
    file = `find . -type f -name '*.zip'`	
    fcrackzip -u -D -p num.list $file
    #find . -type f -name "*.zip" -exec unzip -- '{}' \; -exec rm -- '{}' \;
    pwd = $(cat result | tr -d '\n' | awk '{print $7}')
    unzip -q -P "$pwd" "$file"
    rm $file
done
