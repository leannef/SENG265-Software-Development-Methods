# --- generate_polygon.py
echo -------------------- generate_polygon.py > test_B_stderr.txt
echo --- x0 illegal >> test_B_stderr.txt
python generate_polygon.py x0 250.0 3 2>> test_B_stderr.txt
echo --- y0 illegal >> test_B_stderr.txt
python generate_polygon.py 250.0 y0 3 2>> test_B_stderr.txt
echo --- count illegal >> test_B_stderr.txt
python generate_polygon.py 250.0 250.0 count 2>> test_B_stderr.txt

# triangle
python generate_polygon.py 0.0 250.0 3 > triangle.txt
./lines_to_svg triangle.txt > triangle.svg
# square
python generate_polygon.py 0.0 250.0 4 > square.txt
./lines_to_svg square.txt > square.svg
# pentagon
python generate_polygon.py 0.0 250.0 5 > pentagon.txt
./lines_to_svg pentagon.txt > pentagon.svg

# --- rotate.py
echo -------------------- rotate.py >> test_B_stderr.txt
echo --- angle illegal >> test_B_stderr.txt
python rotate.py a 3 2>> test_B_stderr.txt
echo --- count illegal >> test_B_stderr.txt
python rotate.py 1.0 count 2>> test_B_stderr.txt

python rotate.py 0.39 3 < triangle.txt > triangles.txt
./lines_to_svg triangles.txt > triangles.svg

# --- scale.py
echo -------------------- scale.py >> test_B_stderr.txt
echo --- factor illegal >> test_B_stderr.txt
python scale.py f 3 2>> test_B_stderr.txt
echo --- count illegal >> test_B_stderr.txt
# **** BUG
python scale.py 0.9 count 2>> test_B_stderr.txt

python scale.py 0.9 3 < square.txt > squares.txt
./lines_to_svg squares.txt > squares.svg

# --- translate.py
echo -------------------- translate.py >> test_B_stderr.txt
echo --- delta_x illegal >> test_B_stderr.txt
python translate.py delta_x 250.0 3 2>> test_B_stderr.txt
echo --- delta_y illegal >> test_B_stderr.txt
python translate.py 250.0 delta_y 3 2>> test_B_stderr.txt
echo --- count illegal >> test_B_stderr.txt
python translate.py 250.0 250.0 count 2>> test_B_stderr.txt

python translate.py 0.0 -10.0 3 < pentagon.txt > pentagons.txt
./lines_to_svg pentagons.txt > pentagons.svg
