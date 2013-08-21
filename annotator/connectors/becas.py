


from pprint import pprint
from Bio import Entrez

import becas

def fetch_by_pmid(pmid):

	Entrez.email = "you@example.com"
	Entrez.tool = "test-tool"
	 
	#pmid = 23225384
	handle = Entrez.efetch(db='pubmed', id=pmid, retmode='xml')
	#print(handle.read())
	record = Entrez.read(handle)
	 
	#pprint(record[0]['PubmedData'])

	#pprint(record[0]['MedlineCitation']['Article']['ArticleTitle'])
	title = record[0]['MedlineCitation']['Article']['ArticleTitle']
	#pprint(record[0]['MedlineCitation']['Article']['Abstract']['AbstractText'])
	abstract = record[0]['MedlineCitation']['Article']['Abstract']['AbstractText']
	abstract_text = ""
	for a in abstract:
		abstract_text += a
	print abstract_text
	return (title, abstract_text)

#pprint(fetch_by_pmid(23225384))

def fetch_by_pmid_by_becas(pmid):
	becas.email="bastiao@ua.pt"
	becas.annotate_publication(pmid)
	becas.annotate_publication(23225384, groups={'MRNA':True})
	return (a['title'], a['abstract'])



"""
>>> import becas
>>> becas.email="bastiao@ua.pt"
>>> becas.annotate_publication(23225384)
<Response [200]>
{u'entities_title': [u'Upregulation|UMLS:C0041904:T043:PROC;UMLS:C0041904:T044:PROC|0', u'necrosis|GO:0001906::PROC;GO:0019835::PROC;GO:0008219::PROC;GO:0016271::PROC;GO:0070265::PROC|117', u'Duchenne muscular dystrophy|UMLS:C0013264:T047:DISO|50'], u'publ_date': u'2012 Dec', u'entities_abstract': [u'cells|GO:0005623::COMP|289', u'infiltration|UMLS:C0332448:T046:DISO|42', u'inflammatory cells|UMLS:C0440752:T025:ANAT|276', u'inflammatory responses|GO:0006954::PROC;UMLS:C1155266:T046:DISO|150', u'DMD|UMLS:C0013264:T047:DISO|32', u'Duchenne muscular dystrophy|UMLS:C0013264:T047:DISO|3', u'tissues|UMLS:C0040300:T024:ANAT|302', u'skeletal muscle|UMLS:C0242692:T024:ANAT;UMLS:C1280260:T023:ANAT|58', u'cells|UMLS:C3282337:T025:ANAT;GO:0005623::COMP;UMLS:C0007634:T025:ANAT|84', u'receptor expression|UMLS:C0597360:T045:PROC|346', u'muscle|UMLS:C0026845:T024:ANAT|373', u'DMD|UMLS:C0013264:T047:DISO|369', u'hybridization|UMLS:C0020202:T045:PROC|478', u'CXCL1|UNIPROT:P09341:T116:PRGE|493', u'CD68|UNIPROT:P34810:T116:PRGE|721', u'DMD|UMLS:C0013264:T047:DISO|583', u'muscle|UMLS:C0026845:T024:ANAT|552', u'CCL5|UNIPROT:P13501:T116:PRGE|783', u'blood vessel endothelium|UMLS:C1706972:T024:ANAT|679', u'expressed|UMLS:C1171362:T045:PROC;UMLS:C1515670:T045:PROC;GO:0010467::PROC|741', u'CXCL11|UNIPROT:O14625:T116:PRGE|525', u'CCR2|UNIPROT:P41597:T116:PRGE|650', u'DMD|UMLS:C0013264:T047:DISO|707', u'muscle fibers|GO:0043292::COMP;UMLS:C0242697:T025:ANAT|552', u'CXCL3|UNIPROT:P19876:T116:PRGE|507', u'CXCL12|UNIPROT:P48061:T116:PRGE|606', u'CXCL11|UNIPROT:O14625:T116:PRGE|598', u'ligand|CHEBI:52214:T103:CHED;UMLS:C1749457:T044:PROC;GO:0005488::FUNC|622', u'CCL2|CHEBI:51370:T103:CHED;UNIPROT:P13500:T116:PRGE|645', u'CCL2|CHEBI:51370:T103:CHED;UNIPROT:P13500:T116:PRGE|773', u'CXCL2|UNIPROT:P19875:T116:PRGE|500', u'macrophages|UMLS:C0024432:T025:ANAT|729', u'endothelial chemokine receptors|UNIPROT:Q13829:T116:PRGE|936', u'CXCR1/2/4 ligands|UNIPROT:O75888:T116:PRGE|837', u'muscle fiber|GO:0043292::COMP;UMLS:C0242697:T025:ANAT|867', u'tissue regeneration|GO:0042246::PROC|899', u'macrophages|UMLS:C0024432:T025:ANAT|1018', u'necrosis|GO:0001906::PROC;GO:0019835::PROC;GO:0008219::PROC;GO:0016271::PROC;GO:0070265::PROC|1052', u'muscle|UMLS:C0026845:T024:ANAT|867', u'tissue|UMLS:C0040300:T024:ANAT|899', u'CCL5|UNIPROT:P13501:T116:PRGE|989', u'Upregulation|UMLS:C0041904:T043:PROC;UMLS:C0041904:T044:PROC|920', u'CCL2|CHEBI:51370:T103:CHED;UNIPROT:P13500:T116:PRGE|979', u'endothelial|UMLS:C0014257:T024:ANAT|936', u'expression|GO:0010467::PROC|994', u'fiber|UMLS:C1304649:T024:ANAT|874'], u'country': u'BE', u'abstract': u'In Duchenne muscular dystrophy (DMD), the infiltration of skeletal muscle by immune cells aggravates disease, yet the precise mechanisms behind these inflammatory responses remain poorly understood. Chemotactic cytokines, or chemokines, are considered essential recruiters of inflammatory cells to the tissues.\nWe assayed chemokine and chemokine receptor expression in DMD muscle biopsies (n = 9, average age 7 years) using immunohistochemistry, immunofluorescence, and in situ hybridization.\nCXCL1, CXCL2, CXCL3, CXCL8, and CXCL11, absent from normal muscle fibers, were induced in DMD myofibers. CXCL11, CXCL12, and the ligand-receptor couple CCL2-CCR2 were upregulated on the blood vessel endothelium of DMD patients. CD68(+) macrophages expressed high levels of CXCL8, CCL2, and CCL5.\nOur data suggest a possible beneficial role for CXCR1/2/4 ligands in managing muscle fiber damage control and tissue regeneration. Upregulation of endothelial chemokine receptors and CXCL8, CCL2, and CCL5 expression by cytotoxic macrophages may regulate myofiber necrosis.', u'title': u'Upregulation of chemokines and their receptors in Duchenne muscular dystrophy: potential for attenuation of myofiber necrosis.', u'ids': {u'GO:0001906::PROC': {u'refs': [u'GO:0001906', u'NCI:C16897', u'OMIM:MTHU002552', u'SNOMEDCT:6574001', u'NCIm:C0599733'], u'name': u'cell killing'}, u'GO:0005488::FUNC': {u'refs': [u'GO:0005488', u'NCI:C18219', u'NCIm:C1167622'], u'name': u'binding'}, u'UMLS:C1706972:T024:ANAT': {u'refs': [u'NCI:C53395', u'NCIm:C1706972'], u'name': u'Blood Vessel Endothelium'}, u'UNIPROT:P13501:T116:PRGE': {u'refs': [u'UNIPROT:P13501'], u'name': u'C-C motif chemokine 5'}, u'GO:0016271::PROC': {u'refs': [u'GO:0016271', u'NCI:C16897', u'OMIM:MTHU002552', u'SNOMEDCT:6574001', u'NCIm:C0027540'], u'name': u'tissue death'}, u'CHEBI:52214:T103:CHED': {u'refs': [u'CHEBI:52214'], u'name': u'ligand'}, u'UMLS:C0020202:T045:PROC': {u'refs': [u'SNOMEDCT:81919004', u'NCIm:C0020202'], u'name': u'Crossbreeding'}, u'UMLS:C0041904:T044:PROC': {u'refs': [u'NCIm:C0041904'], u'name': u'Up-Regulation (Physiology)'}, u'UNIPROT:P48061:T116:PRGE': {u'refs': [u'UNIPROT:P48061'], u'name': u'SDF-1'}, u'UMLS:C1280260:T023:ANAT': {u'refs': [u'SNOMEDCT:244716004', u'NCIm:C1280260'], u'name': u'Entire skeletal muscle (organ)'}, u'GO:0019835::PROC': {u'refs': [u'GO:0019835', u'NCI:C61553', u'OMIM:MTHU003072', u'SNOMEDCT:239551005', u'NCIm:C1536403'], u'name': u'cytolysis'}, u'UMLS:C1749457:T044:PROC': {u'refs': [u'NCIm:C1749457'], u'name': u'ligands activity'}, u'UNIPROT:P34810:T116:PRGE': {u'refs': [u'UNIPROT:P34810'], u'name': u'Macrosialin'}, u'UNIPROT:Q13829:T116:PRGE': {u'refs': [u'UNIPROT:Q13829'], u'name': u'BTB/POZ domain-containing protein TNFAIP1'}, u'UMLS:C0597360:T045:PROC': {u'refs': [u'NCIm:C0597360'], u'name': u'receptor expression'}, u'UMLS:C0242697:T025:ANAT': {u'refs': [u'NCIm:C0242697'], u'name': u'Muscle Fibers'}, u'UMLS:C1304649:T024:ANAT': {u'refs': [u'NCIm:C1304649', u'FMA:Fiber'], u'name': u'Tissue fiber'}, u'UNIPROT:O14625:T116:PRGE': {u'refs': [u'UNIPROT:O14625'], u'name': u'C-X-C motif chemokine 11'}, u'GO:0005623::COMP': {u'refs': [u'GO:0005623', u'NCI:C12508', u'NCIm:C0007634', u'SNOMEDCT:4421005', u'FMA:Normal_cell'], u'name': u'cell'}, u'UMLS:C0440752:T025:ANAT': {u'refs': [u'SNOMEDCT:256923004', u'NCIm:C0440752'], u'name': u'Inflammatory cell'}, u'GO:0070265::PROC': {u'refs': [u'GO:0070265', u'NCI:C16897', u'OMIM:MTHU002552', u'SNOMEDCT:6574001', u'NCIm:C0027540'], u'name': u'necrotic cell death'}, u'GO:0010467::PROC': {u'refs': [u'GO:0010467', u'NCI:C16608', u'SNOMEDCT:89551006', u'NCIm:C0017262'], u'name': u'gene expression'}, u'UMLS:C0026845:T024:ANAT': {u'refs': [u'NCI:C12435', u'NCIm:C0026845', u'SNOMEDCT:91727004', u'FMA:Muscle_organ'], u'name': u'Muscle'}, u'UMLS:C0041904:T043:PROC': {u'refs': [u'NCIm:C0041904'], u'name': u'Up-Regulation (Physiology)'}, u'UNIPROT:P13500:T116:PRGE': {u'refs': [u'UNIPROT:P13500'], u'name': u'C-C motif chemokine 2'}, u'UNIPROT:P19876:T116:PRGE': {u'refs': [u'UNIPROT:P19876'], u'name': u'C-X-C motif chemokine 3'}, u'UMLS:C0007634:T025:ANAT': {u'refs': [u'NCI:C12508', u'NCIm:C0007634', u'SNOMEDCT:4421005', u'FMA:Set_of_cells'], u'name': u'Cells'}, u'UMLS:C0013264:T047:DISO': {u'refs': [u'NCI:C75482', u'SNOMEDCT:76670001', u'omim.org:302045', u'NCIm:C0013264'], u'name': u'Muscular Dystrophy, Duchenne'}, u'UMLS:C3282337:T025:ANAT': {u'refs': [u'NCIm:C3282337'], u'name': u'Cells [Chemical/Ingredient]'}, u'GO:0042246::PROC': {u'refs': [u'GO:0042246', u'NCIm:C1623047'], u'name': u'tissue regeneration'}, u'UMLS:C0332448:T046:DISO': {u'refs': [u'NCI:C25754', u'SNOMEDCT:47351003', u'NCIm:C0332448'], u'name': u'Infiltration'}, u'UNIPROT:P19875:T116:PRGE': {u'refs': [u'UNIPROT:P19875'], u'name': u'C-X-C motif chemokine 2'}, u'UNIPROT:P41597:T116:PRGE': {u'refs': [u'UNIPROT:P41597'], u'name': u'C-C chemokine receptor type 2'}, u'UMLS:C0242692:T024:ANAT': {u'refs': [u'NCI:C13050', u'NCIm:C0242692', u'SNOMEDCT:127954009', u'FMA:Skeletal_muscle_tissue'], u'name': u'Skeletal muscle structure'}, u'GO:0043292::COMP': {u'refs': [u'GO:0043292', u'NCIm:C1752744'], u'name': u'contractile fiber'}, u'GO:0008219::PROC': {u'refs': [u'GO:0008219', u'NCI:C16897', u'OMIM:MTHU002552', u'SNOMEDCT:6574001', u'NCIm:C0027540'], u'name': u'cell death'}, u'UMLS:C0024432:T025:ANAT': {u'refs': [u'NCI:C12558', u'NCIm:C0024432', u'SNOMEDCT:58986001', u'FMA:Macrophage'], u'name': u'macrophage'}, u'UMLS:C0014257:T024:ANAT': {u'refs': [u'NCI:C12481', u'NCIm:C0014257', u'SNOMEDCT:27168002', u'FMA:Endothelium'], u'name': u'Endothelium'}, u'CHEBI:51370:T103:CHED': {u'refs': [u'CHEBI:51370'], u'name': u'dichlorocarbene'}, u'UMLS:C1155266:T046:DISO': {u'refs': [u'NCI:C20151', u'NCIm:C1155266'], u'name': u'Inflammatory Response'}, u'UNIPROT:O75888:T116:PRGE': {u'refs': [u'UNIPROT:O75888'], u'name': u'Tumor necrosis factor ligand superfamily member 13'}, u'UMLS:C0040300:T024:ANAT': {u'refs': [u'NCI:C12801', u'NCIm:C0040300', u'SNOMEDCT:85756007', u'FMA:Portion_of_tissue'], u'name': u'Body tissue'}, u'UNIPROT:P09341:T116:PRGE': {u'refs': [u'UNIPROT:P09341'], u'name': u'Growth-regulated alpha protein'}, u'GO:0006954::PROC': {u'refs': [u'GO:0006954', u'NCI:C20151', u'NCIm:C1155266'], u'name': u'inflammatory response'}, u'UMLS:C1515670:T045:PROC': {u'refs': [u'NCI:C18888', u'NCIm:C1515670'], u'name': u'mRNA Expression'}, u'UMLS:C1171362:T045:PROC': {u'refs': [u'NCI:C18966', u'NCIm:C1171362'], u'name': u'protein expression'}}, u'authors': [u'De Paepe B', u'Creus KK', u'Martin JJ', u'De Bleecker JL'], u'doi': u'10.1002/mus.23481', u'publ_type': [u'Journal Article', u"Research Support, Non-U.S. Gov't"], u'jrn_title': u'Muscle Nerve', u'pmid': u'23225384'}
>>> becas.annotate_publication(23225384, groups={'MRNA':True})
<Response [200]>
{u'entities_title': [], u'publ_date': u'2012 Dec', u'entities_abstract': [], u'country': u'BE', u'abstract': u'In Duchenne muscular dystrophy (DMD), the infiltration of skeletal muscle by immune cells aggravates disease, yet the precise mechanisms behind these inflammatory responses remain poorly understood. Chemotactic cytokines, or chemokines, are considered essential recruiters of inflammatory cells to the tissues.\nWe assayed chemokine and chemokine receptor expression in DMD muscle biopsies (n = 9, average age 7 years) using immunohistochemistry, immunofluorescence, and in situ hybridization.\nCXCL1, CXCL2, CXCL3, CXCL8, and CXCL11, absent from normal muscle fibers, were induced in DMD myofibers. CXCL11, CXCL12, and the ligand-receptor couple CCL2-CCR2 were upregulated on the blood vessel endothelium of DMD patients. CD68(+) macrophages expressed high levels of CXCL8, CCL2, and CCL5.\nOur data suggest a possible beneficial role for CXCR1/2/4 ligands in managing muscle fiber damage control and tissue regeneration. Upregulation of endothelial chemokine receptors and CXCL8, CCL2, and CCL5 expression by cytotoxic macrophages may regulate myofiber necrosis.', u'title': u'Upregulation of chemokines and their receptors in Duchenne muscular dystrophy: potential for attenuation of myofiber necrosis.', u'ids': {}, u'authors': [u'De Paepe B', u'Creus KK', u'Martin JJ', u'De Bleecker JL'], u'doi': u'10.1002/mus.23481', u'publ_type': [u'Journal Article', u"Research Support, Non-U.S. Gov't"], u'jrn_title': u'Muscle Nerve', u'pmid': u'23225384'}
>>> a = becas.annotate_publication(23225384, groups={'MRNA':True})
<Response [200]>

>>> becas.annotate_publication(23225384, groups={'MRNA':True})
>>> a['title']
>>>
>>> a['abstract']
"""