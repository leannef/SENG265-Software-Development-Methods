# $# is the number of command line arguments, NOT including the script name
# $1: is the first argument, AFTER the script itself

if [ $# -ne 1 ];
	then echo "Syntax python three_rings.sh number_of_sides"
	exit
fi

# polygon at origin as basis for all others
python generate_polygon.py 0.0 50.0 $1 > polygon.txt

# generate top polygon 
python translate.py 0.0 200.0 1 < polygon.txt > polygon_top.txt

# generate middle polygon 
python scale.py 0.8 1 < polygon.txt > polygon_middle0.txt
python translate.py 0.0 110.0 1 < polygon_middle0.txt > polygon_middle1.txt

# generate bottom polygon 
python scale.py 0.5 1 < polygon.txt > polygon_bottom0.txt
python translate.py 0.0 45.0 1 < polygon_bottom0.txt > polygon_bottom1.txt

# combine 3 polygons and rotate
cat polygon_top.txt polygon_middle1.txt polygon_bottom1.txt > three_rings0.txt
python rotate.py 0.395 16 < three_rings0.txt > three_rings.txt

# generate SVG
./lines_to_svg three_rings.txt > three_rings.svg
