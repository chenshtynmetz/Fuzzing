# Fuzzing
In this task we asked to warn on suspected fuzzing attack.
In the main i sniff packet with scapy library with filter: "tcp port 22" in order to catch only ssh packets.
When packet is caught i check some conditions to check if this fuzzing.
