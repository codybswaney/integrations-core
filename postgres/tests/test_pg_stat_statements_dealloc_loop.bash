x=0
while [ $x -le 100 ]; 
do 
    ddev test postgres:py3.8-14.0 -k test_pg_stat_statements_dealloc --skip-env
    ((x++))
done
