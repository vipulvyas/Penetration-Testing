#!/usr/bin/perl -w

my $hash=$ARGV[0];
# The hash is encoded as base64 twice:
use MIME::Base64;
$hash = decode_base64($hash);
$hash=~s/{SSHA}//;
$hash = decode_base64($hash);

# The salt length is four (the last four bytes).
$salt = substr($hash, -4);

# Split the salt into an array.
my @bytes = split(//,$salt);

# Convert each byte from binary to a human readable hexadecimal number.
foreach my $byte (@bytes) {
$byte = uc(unpack "H*", $byte);
print "$byte";
}
