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
unzip "$problempath/$problem.zip" -d "$problempath"
rm "$problempath/$problem.zip"
touch "$problempath/$problem.py"