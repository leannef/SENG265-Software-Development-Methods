#include<stdio.h>
#include<string.h>

// SVG header with placeholders for canvas width and height
char SVG_HEADER[] =
	"<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\""
		" width=\"%d\" height=\"%d\">\n";

// SVG bounding box with placeholders for width and height
char SVG_BOUNDING_BOX[] =
	"<rect x=\"0\" y=\"0\" width=\"%d\" height=\"%d\""
		" style=\"stroke:#000;fill:none\" />\n";

// SVG line with placeholders for x0, y0, x1, y1
char SVG_LINE[] =
	"<line x1=\"%d\" y1=\"%d\" x2=\"%d\" y2=\"%d\""
	" style=\"stroke:#000\" />\n";

// SVG footer
char SVG_FOOTER[] = "</svg>";

#define CANVAS_HEIGHT 500
#define CANVAS_WIDTH 500

int main(int argc, char* argv[])
{
	int n, x0, y0, x1, y1;

	int BUFFER_LENGTH = 80;
	char buffer[BUFFER_LENGTH];
	char keyword[BUFFER_LENGTH];
	int line_number = 1;
	FILE *lines_file;

	// process command line arguments
	if (argc != 2) {
		fprintf(stderr, "Usage: %s lines_file\n", argv[0]);
		return 1;
	}
	lines_file = fopen(argv[1], "r");
	if (lines_file == NULL) {
		fprintf(stderr, "Cannot open: %s\n", argv[1]);
		return 2;
	}

	// generate header, bounding box
	printf(SVG_HEADER, CANVAS_WIDTH, CANVAS_HEIGHT);
	printf(SVG_BOUNDING_BOX, CANVAS_WIDTH, CANVAS_HEIGHT);

	// process lines file until end of file, or an error
	while (fgets(buffer, BUFFER_LENGTH, lines_file) != NULL) {
		line_number++;
		n = sscanf(buffer, "%s %d %d %d %d",
		 keyword, &x0, &y0, &x1, &y1);
		if (n != 5) {
			fprintf(stderr, "Error in line %d: %s\n",
			 line_number,buffer);
			return 5;
		}

		// convert from standard to SVG coordinates
		// TODO: check that w/h are even?
		x0 += CANVAS_WIDTH/2;
		y0 = -y0 + CANVAS_HEIGHT/2;
		x1 += CANVAS_WIDTH/2;
		y1 = -y1 + CANVAS_HEIGHT/2;

		if (
			x0 < 0 || x0 > CANVAS_WIDTH ||
			y0 < 0 || y0 > CANVAS_HEIGHT
			||
			x1 < 0 || x1 > CANVAS_WIDTH ||
			y1 < 0 || y1 > CANVAS_HEIGHT
		) {
			fprintf(stderr, "Error in line %d: %s\n",
			 line_number, buffer);
			return 6;
		}

		printf(SVG_LINE, x0, y0, x1, y1);
	}
	printf("%s\n", SVG_FOOTER);
	
	return 0;
}
