import pandas as pd
from Bio import Entrez
from Bio.Seq import Seq
from arg_receiver import arg_handler
import data_parsing as dp


def main():
	#Se recive el query desde la linea de comando
	query,email,retmax=arg_handler()
	
	Entrez.email = email
	handleSearch = Entrez.esearch(db="Nucleotide", retmax=retmax, term=query)
	rec = Entrez.read(handleSearch)

	idlist = rec["IdList"]
	data = []

	#For each id, use Entrez.efetch() to get the record with type gb, and retmote xml.
	for idr in idlist:
		print(idr)
		handleFetch = Entrez.efetch(db="nucleotide", retype="gb" ,id=idr, retmode="xml")
		record = Entrez.parse(handleFetch).__next__()
		print("polish record executed...")
		record = dp.polish_record(record)
		
		data.append(list(record.values()))

	dfObj=pd.DataFrame(data,columns=['GBSeq_locus', 'GBSeq_length', 'GBSeq_strandedness', 'GBSeq_moltype', 'GBSeq_topology', 'GBSeq_division', 'GBSeq_source', 'GBSeq_organism', 'GBSeq_taxonomy', 'GBSeq_sequence','GB_A_count','GB_T_count','GB_G_count','GB_C_count','GBProtein_translation'])

	dfObj.to_csv("final_data.csv",sep='\t')


main()
