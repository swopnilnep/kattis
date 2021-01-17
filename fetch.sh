while getopts p:l: flag
do
    case "${flag}" in
        l) language=${OPTARG};;
        p) problem=${OPTARG};;
    esac
done
echo "Fetching problem: $problem";

problempath="./python3/$problem"
mkdir $problempath
echo "Created $problempath"

curl "https://open.kattis.com/problems/$problem/file/statement/samples.zip" --output "$problempath/$problem.zip"
mkdir "$problempath/samples"
unzip "$problempath/$problem.zip" -d "$problempath/samples"
rm "$problempath/$problem.zip"
touch "$problempath/$problem.py"

echo "
$problem
Author: Swopnil Shrestha https://open.kattis.com/users/shresw01
Problem: https://open.kattis.com/problems/$problem
Execution: python3 $problem.py < ./samples/<sample>.in
" > "$problempath/readme.txt"