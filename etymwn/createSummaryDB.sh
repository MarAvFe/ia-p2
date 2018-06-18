tail -n 6031431 ../etymwn/etymwn.tsv | cut -d$'\t' -f2 | sort | uniq > rels
touch ./summaryDBtmp.tsv
while read line
do
	echo "Filtering by $line..."
	grep $line ../etymwn/etymwn.tsv | head -n 20000 >> ./summaryDBtmp.tsv
done < rels

grep "avis" ../etymwn/etymwn.tsv | head -n 20000 >> ./summaryDBtmp.tsv
grep "aviarus" ../etymwn/etymwn.tsv | head -n 20000 >> ./summaryDBtmp.tsv
grep "aviarium" ../etymwn/etymwn.tsv | head -n 20000 >> ./summaryDBtmp.tsv
grep "aviation" ../etymwn/etymwn.tsv | head -n 20000 >> ./summaryDBtmp.tsv
tail ./summaryDBtmp.tsv
grep "rel:" ./summaryDBtmp.tsv | sort | uniq > ./summaryDB.tsv
rm ./summaryDBtmp.tsv

echo "File ./summaryDB.tsv succesfully created."
