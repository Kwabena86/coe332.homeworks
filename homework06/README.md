               i                                GENES APPLICATION(APP)
The project is to write an application to provide data about genes and its idenification (IDs)


                                                DATA ACCESSED
The data accessed for the project from the link https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json. The url link is loaded into the script through API request from the python requests library.The dataset includes information for all HGNC genes.The site link will help users learn more about the data used in other for the user to understand the application.Refer to this link https://www.genenames.org/download/archive/.

                                                 INSTALLING DEPENDENCIES
import requets
import json

https://ftp.ebi.ac.uk/pub/databases/genenames/hgnc/json/hgnc_complete_set.json
response = requests.get(url)


                                                 INSTRUCTIOS AND FLASK APPLICATION

This Flask application that runs the application on the local port. The application will queries data form the this link listed above.The curl route will be used to run the data sets in other to get our requests from the Flask application. The Routes used are as follows.
                                                  INSTRUCTION TO RUN TO PULL IMAGES FROM DOCKERHUP

1 Docker images should be pulled from dockerhub in other for the application to run, to pull docker images,the following command should be run on a separate terminal.
  
  docker pull boatengsam/genes:1.0

2 After the docker image is pulled,the following command shold be run.
  
  docker-compose up

                                                  INSTRUCTIONS TO RUN TO BUILD DOCKERFILE

After the image is pulled,images are build by exercuting the following command:

  docker build -t username/genes:tag

Run the Flask application using the newly built image change the image name in yaml file

version: "3"

services:
    redis-db:
        image: redis:7
        ports:
            - 6379:6379
        volumes:
           - ./data:/data
        user: "1000:1000"
    flask-app:
        build:
            context: ./
            dockerfile: ./Dockerfile
        depends_on:
            - redis-db
        image: boatengsam/genes:1.0
        ports:
            - 5000:5000
        volumes:
           - ./config.yaml:/config.yaml

The last thing to do is to run: docker-compose up


NOTE:For the appilication to start running,data must be loaded into the redis database using the data post before the other curl commands work. 
                                                
                                                    ROUTES TO EXERCUTE


 ROUTES                       METHOD                        RETURS(OUTPUTS)

   /data                       GET                  The entire Dataset

   /data                       POST                 Confirm a set of message of posted data from redis-database

   /data                       DELETE               Confirm a set of message of deleted data from redis database

   /genes                      GET                  List of all HGNC_IDs in the set

   /genes/<hgnc_id>            GET                  Dictionary of the relevant data from the specific HGNC_ID genes.


                                                   INSTRUCTIONS TO RUN
Data must be loaded into the redis database by using the post command in other to impliment application.

                                      ROUTES COMMANDS USING CURL
1 curl 'localhost:5000/data'
 
The command should return the whole dataset which looks like the following
 ],
    "pseudogene.org": "PGOHUM00000233900",
    "refseq_accession": [
      "NG_029070"
    ],
    "status": "Approved",
    "symbol": "TSPY17P",
    "uuid": "5dfd779e-9ed7-4234-93c7-ded35956a6bf",
    "vega_id": "OTTHUMG00000036523"
  },
  {
    "_version_": 1761599367310999552,
    "agr": "HGNC:3416",
    "alias_symbol": [
      "EPO-R"
    ],
    "ccds_id": [
      "CCDS12260"
    ],
    "date_approved_reserved": "1990-05-14",
    "date_modified": "2023-01-23",
    "ena": [
      "M34986"
    ],
    "ensembl_gene_id": "ENSG00000187266",
    "entrez_id": "2057",
    "gencc": "HGNC:3416",
    "gene_group": [
      "Fibronectin type III domain containing"
    ],
    "gene_group_id": [
      555
    ],
    "hgnc_id": "HGNC:3416",
    "iuphar": "objectId:1718",
    "location": "19p13.2",
    "location_sortable": "19p13.2",
    "locus_group": "protein-coding gene",
    "locus_type": "gene with protein product",
    "mane_select": [
      "ENST00000222139.11",
      "NM_000121.4"
    ],
    "mgd_id": [
      "MGI:95408"
    ],
    "name": "erythropoietin receptor",
    "omim_id": [
      "133171"
    ],
    "orphanet": 121581,
    "pubmed_id": [
      9192789,
      2163696
    ],
    "refseq_accession": [
      "NM_000121"
    ],
    "rgd_id": [
      "RGD:2560"
    ],



2 curl -X POST 'localhost:5000/data'

This command should return the following:

Data had neen deleted. There are 0 keys in the db



3 curl -X POST 'localhost:5000/data'

This command should return the following:

Data has been posted



4 curl localhost:5000/genes

The command should return a list of the gene IDs in the dataset:

 "HGNC:15663",
  "HGNC:53224",
  "HGNC:50762",
  "HGNC:4703",
  "HGNC:27320",
  "HGNC:12945",
  "HGNC:30869",
  "HGNC:29283",
  "HGNC:3774",
  "HGNC:13109",
  "HGNC:6891",
  "HGNC:10456",
  "HGNC:27905",
  "HGNC:44571",
  "HGNC:15223",
  "HGNC:41049",
  "HGNC:2194",
  "HGNC:39742",
  "HGNC:25401",
  "HGNC:10084",
  "HGNC:49804",
  "HGNC:11266",
  "HGNC:7693",
  "HGNC:35829",
  "HGNC:9936",
  "HGNC:30162",
  "HGNC:12607",


5 curl localhost:5000/genes/HGNC:15663

This command should return the following:

:38949",
  "_version_": 1761599403115675648,
  "agr": "HGNC:15663",
  "alias_symbol": [
    "HUGT1"30",
  ],GNC:21338",
  "ccds_id": [,
    "CCDS2154",
  ],GNC:28589",
  "date_approved_reserved": "2001-06-05",
  "date_modified": "2023-03-15",
  "date_name_changed": "2009-07-23",
  "date_symbol_changed": "2009-07-23",
  "ena": [240",
    "AF227905",
  ],GNC:32747",
  "ensembl_gene_id": "ENSG00000136731",
  "entrez_id": "56886",
  "gene_group": [
    "UDP-glucose glycoprotein glucosyltransferases"
  ],GNC:45007",
  "gene_group_id": [
    440:23106",
  ],GNC:34395",
  "hgnc_id": "HGNC:15663",
  "location": "2q14.3",
  "location_sortable": "02q14.3",
  "locus_group": "protein-coding gene",
  "locus_type": "gene with protein product",
  "mane_select": [
    "ENST00000259253.11",
    "NM_020120.4"
  ],GNC:54919",
  "mgd_id": [,
    "MGI:2443162"
  ],GNC:26616",
  "name": "UDP-glucose glycoprotein glucosyltransferase 1",
  "omim_id": [,
    "605897"9",
  ],GNC:5888",
  "prev_name": [
    "UDP-glucose ceramide glucosyltransferase-like 1"
  ],GNC:26895",
  "prev_symbol": [
    "UGCGL1"0",
  ],GNC:23287",
  "pubmed_id": [
    106943803",
  ],GNC:22991",
  "refseq_accession": [
    "NM_020120"
  ],GNC:18306",
  "rgd_id": [",
    "RGD:619710"
  ],GNC:44254",
  "status": "Approved",
  "symbol": "UGGT1",
  "ucsc_id": "uc002tps.4",
  "uniprot_ids": [
    "Q9NYU2"5",
  ],GNC:18611",