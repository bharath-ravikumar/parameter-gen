for i in {1901..2300}
do
cd run$i
paste Data.txt Conc.txt > Finaldata.txt
cd ..
done
