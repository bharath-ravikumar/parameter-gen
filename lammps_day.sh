for L2 in {286..300}
do
rm -r run$L2
mkdir run$L2 
cp *.py in.mdpd surface.in.mdpd run$L2/.
cd run$L2/
python3 ./createatoms.py 4128457
mpirun -np 96 ~/sharedscratch/lammps-29Aug2024/src/lmp_mpi -in in.mdpd > log1.out
grep 220000 'log.lammps'| awk '{print $4, $8, $18}' > Xdata0.txt 
tail Sc.txt -n 1| awk '{print $2,$3}' > Ydata.txt 
python3 ./paramextract.py 
mpirun -np 96 ~/sharedscratch/lammps-29Aug2024/src/lmp_mpi -in surface.in.mdpd > log2.out
tail ST.txt -n 1| awk '{print $2,$3}' > Ydata2.txt 
paste Ydata2.txt Ydata.txt Xdata0.txt Xdata1.txt > Data.txt 
cd ../
done

 
