######################################################################
# Author: Dr. Scott Heggen             TODO: Change this to your names
# Username: heggens                    TODO: Change this to your usernames
#
# Assignment: HW08: It's in Your Genes
#
# Purpose: A test suite to test the a06_genes code
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
#   Idea from: http://www.cs.uni.edu/~schafer/1140/assignments/pa9/index.htm
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

from inspect import getframeinfo, stack

from hw08_genes import *


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


def genomics_test_suite():
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

    # TODO   We highly suggest starting by building more test cases for each function.
    # TODO   If you can build accurate test cases, you can be confident that you understand
    # TODO   the intended functionality of each function.

    # The following tests test the is_nucleotide() function
    print("Testing is_nucleotide()")
    unittest(is_nucleotide("CGTAGGCAT") == True)
    unittest(is_nucleotide("CGTAFLCAT") == False)
    # FIXME: Add your own tests here

    # Testing the complement_strand() function
    print("\nTesting complement_strand()")
    unittest(complement_strand("CC") == "GG")
    unittest(complement_strand("CA") == "GT")
    unittest(complement_strand("CGTAGGCAT") == "GCATCCGTA")
    unittest(complement_strand("CGTAFLCAT") == "Sequencing Error")
    # FIXME: Add your own tests here

    # Testing the mRNA() function
    print("\nTesting mRNA()")
    unittest(mRNA("GCATCCGTA") == "GCAUCCGUA")
    unittest(mRNA("CCATTGGGTT") == "CCAUUGGGUU")
    unittest(mRNA("AAGCACCG") == "AAGCACCG")
    # FIXME: Add your own tests here

    # Testing chunk_amino_acid()
    print("\nTesting chunk_amino_acid()")
    unittest(chunk_amino_acid("CGUCAC") == ["CGU","CAC"])
    unittest(chunk_amino_acid("CGUAGGCAUUU") == ["CGU","AGG","CAU"])      # note that the "extra two U's are discarded
    # FIXME: Add your own tests here

    # Testing amino_acid_chunks()
    print("\nTesting amino_acid_chunks()")
    unittest(translate_amino_acid('AGA') == 'R')
    unittest(translate_amino_acid('AFA') == '?')
    # FIXME: Add your own tests here.

    # Testing sequence_gene()
    print("\nTesting sequence_gene()")
    unittest(sequence_gene("T") == '')            # because input is not in a group of 3 nucleotides
    unittest(sequence_gene("JAN") == '')          # because input is not a valid string of nucleotides
    unittest(sequence_gene("CACGT") == 'V')       # because mRNA sequence is "GUGCA"
                                                # and ignoring the last two "extra" nucleotides,
                                                # this returns amino acid "V".
    unittest(sequence_gene("CGTAGGCAT") == "ASV") # because mRNA sequence is "GCAUCCGUA"
                                                # taking the complement and then replacing the T nucleotide with U.
                                                # Grouping into triples, we  get the "ASV" amino acid sequence.

def main():
    genomics_test_suite()


main()
