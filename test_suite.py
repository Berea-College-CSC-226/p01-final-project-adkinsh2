######################################################################
# Author: Harry Adkins
# Username: adkinsh2
#
# Assignment: Final Project
#
# Purpose: A test suite to test the a06_genes code
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

from inspect import getframeinfo, stack
from final_project import Game

def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def game_test_suite():
    """
    The genomics_test_suite() is designed to test the following:
      is_nucleotide(sequence)
      complement_strand()
      mRNA()
      chunk_amino_acid()
      amino_acid_chunks()
      sequence_gene()

    :return: None
    """
    # Testing the complement_strand() function
    print("\nTesting complement_strand()")

def main():
    game_test_suite()

main()