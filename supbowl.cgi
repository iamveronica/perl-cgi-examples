#!/usr/bin/perl
#supbowl.cgi - saves form data to a file, and creates a dynamic
#Web page that displays a message and survey statistics
print "Content-type: text/html\n\n";
use CGI qw(:standard -debug);
use strict;

#declare variables
my ($game, $commercial, $size, @records, @errors);
my @game_count = (0, 0, 0);
my %comm_count = ("Budweiser", 0,
		  "FedEx", 0,
		  "MasterCard", 0,
		  "Pepsi", 0);

#assign input items to variables
$game = param('Game');
$commercial = param('Commercial');

#validate input data
if ($game ne "0" and $game ne "1" and $game ne "2") {
	push(@errors, "Select a button from the Game section");
}

if ($commercial ne "Budweiser" and $commercial ne "FedEx" and $commercial ne "MasterCard" 
and $commercial ne "Pepsi") {
	push(@errors, "Select a button from the Commercial section");
}

#determine size of @errors array
$size = @errors;


#process input data or display error page
if ($size == 0) {
	#process input data
	#save form data to a file
	open(OUTFILE, ">>", "survey.txt") 
		or die "Error opening survey.txt. #!, stopped";
	print OUTFILE "$game,$commercial\n";
	close(OUTFILE);

	#calculate survey statistics
	open(INFILE, "<", "survey.txt") 
		or die "Error opening survey.txt. $!, stopped";
	@records = <INFILE>;
	close(INFILE);
	foreach my $rec (@records) {
		chomp($rec);
		($game, $commercial) = split(/,/, $rec);
		$game_count[$game] = $game_count[$game] + 1;
		$comm_count{$commercial} = $comm_count{$commercial} + 1;
	}

	#generate HTML acknowledgment
	print "<HTML><HEAD><TITLE>WKRK-TV</TITLE></HEAD>\n";
	print "<BODY>\n";
	print "<H2>Thank you for participating in our survey.</H2>\n";

	print "<EM><B>What did you think of the Super Bowl game?</EM></B>\n";
	print "<TABLE>\n";
	print "<TR><TD>It was a great game.</TD>    <TD>$game_count[0]</TD></TR>\n";
	print "<TR><TD>It was a boring game.</TD>   <TD>$game_count[1]</TD></TR>\n";
	print "<TR><TD>I didn't watch the game.</TD><TD>$game_count[2]</TD></TR>\n";
	print "</TABLE><BR>\n";

	print "<EM><B>Vote for your favorite Super Bowl commercial:</EM></B>\n";
	print "<TABLE>\n";
	foreach my $key ("Budweiser", "FedEx", "MasterCard", "Pepsi") {
		print "<TR><TD>$key</TD>  <TD>$comm_count{$key}</TD></TR>\n";
	}
	print "</TABLE>\n";
	print "</BODY></HTML>\n";
}
else {
	#display error page
	print "<html><head><title>WKRK-TV</title></head>\n";
	print "<body>\n";
	print "<h2>Please press your browser's back button to \n";
	print "return to the survey, then: </h2><br/>\n";
	for(my $x = 0; $x < $size; $x = $x + 1) {
		print "$errors[$x]<br/>\n";
	}
	print "</body></html>\n";
}