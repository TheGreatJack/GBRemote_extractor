#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 20:45:37 2021

@author: anderjackf
"""

from Bio.Seq import Seq

def polish_record(record):
	relevant_keys=['GBSeq_locus', 'GBSeq_length', 'GBSeq_strandedness', 'GBSeq_moltype', 'GBSeq_topology', 'GBSeq_division', 'GBSeq_source', 'GBSeq_organism', 'GBSeq_taxonomy', 'GBSeq_sequence']
	
	summary_record={}
	
	for key in relevant_keys:
		try:
			summary_record[key]=record[key]
		except KeyError:
			summary_record[key]="-"
	
	print("conteo de nucleotidos...")
	summary_record=add_counts(summary_record)
	print("traduccion...")
	summary_record=add_prot_seq(summary_record)
	
	return summary_record
	
def add_counts(summary_record):
	a_count=summary_record['GBSeq_sequence'].count("A") + summary_record['GBSeq_sequence'].count("a")
	t_count=summary_record['GBSeq_sequence'].count("T") + summary_record['GBSeq_sequence'].count("t")
	g_count=summary_record['GBSeq_sequence'].count("G") + summary_record['GBSeq_sequence'].count("g")
	c_count=summary_record['GBSeq_sequence'].count("C") + summary_record['GBSeq_sequence'].count("c")

	summary_record["GB_A_count"]=a_count
	summary_record["GB_T_count"]=t_count
	summary_record["GB_G_count"]=g_count
	summary_record["GB_C_count"]=c_count

	return summary_record


def add_prot_seq(summary_record):
	prot_seq=str(Seq(summary_record["GBSeq_sequence"]).translate())
	summary_record["GBProtein_translation"]=prot_seq

	return summary_record
