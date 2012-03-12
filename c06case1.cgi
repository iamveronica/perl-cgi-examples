#!/usr/bin/perl
print "Content-type: text/html\n\n";
use CGI qw(:standard -debug);
use strict;

#declare variables
my ($name, $p1, $p2, $mid, $fin, $size, $total, @records, @errors);

#assign input items to variables
$name = param('Name');
$p1 = param('P1');
$p2 = param('P2');
$mid = param('Midterm');
$fin = param('Final');

#validate input data
if ($name eq "") {
	push(@errors, "<b>Student Name</b> was not entered.");
}

if ($p1 < 0 or $p1 > 50 or $p1 eq "") {
	push(@errors, "Invalid point amount entered for <b>Project 1</b>.");
}

if ($p2 < 0 or $p2 > 50 or $p2 eq "") {
	push(@errors, "Invalid point amount entered for <b>Project 2</b>.");
}

if ($mid < 0 or $mid > 100 or $mid eq "") {
	push(@errors, "Invalid point amount entered for <b>Midterm</b>.");
}

if ($fin < 0 or $fin > 100 or $fin eq "") {
	push(@errors, "Invalid point amount entered for <b>Final</b>.");
}

#determine size of @errors array
$size = @errors;


#process input data or display error page
if ($size == 0) {
	#process input data
	#save form data to a file
	open(OUTFILE, ">>", "c06case1.txt") 
		or die "Error opening c06case1.txt. #!, stopped";
	print OUTFILE "$name,$p1,$p2,$mid,$fin\n";
	close(OUTFILE);

	#calculate survey statistics
	open(INFILE, "<", "c06case1.txt") 
		or die "Error opening c06case1.txt. $!, stopped";
	@records = <INFILE>;
	close(INFILE);
	chomp(@records);
	$total = $p1 + $p2 + $mid + $fin;
		 
		

	#generate HTML acknowledgment
	print "<HTML><HEAD><TITLE>Mountain Community College</TITLE></HEAD>\n";
	print "<BODY>\n";
	print "<H2>The following record was saved:</H2>\n";
    print "<table><tr><td><b>Student Name:</b></td><td> $name </td></tr>\n";
    print "<tr><td><b>Total Points:</b></td><td> $total </td></tr></table>\n";
    print "<a href='http://veganbunny.com/homework/c06case1.html'><br/>Back To The Form</a>\n";
	print "</BODY></HTML>\n";
}
else {
	#display error page
	print "<html><head><title>Mountain Community College</title></head>\n";
	print "<body>\n";
	print "<h2>The following errors were found in the data entered on the form: </h2>\n";
	for(my $x = 0; $x < $size; $x = $x + 1) {
		print "$errors[$x]<br/>\n";
	}
	print "<a href='http://veganbunny.com/homework/c06case1.html'><br/>Back To The Form</a>\n";
	print "</body></html>\n";
}