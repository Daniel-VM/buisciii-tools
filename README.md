# buisciii-tools

[![python_lint](https://github.com/BU-ISCIII/buisciii-tools/actions/workflows/python_lint.yml/badge.svg)](https://github.com/BU-ISCIII/buisciii-tools/actions/workflows/python_lint.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

BU-ISCIII provides a serie or services in its portfolio for supporting bioinformatics analysis to the labs in the Institute of Health Carlos III. bu-isciii tools is a set of helper tools for management of these bioinformatics analysis together with the LIMS ([iSkyLIMS](https://github.com/BU-ISCIII/iSkyLIMS))

- [buisciii-tools](#buisciii-tools)
  - [Installation](#installation)
    - [Bioconda](#bioconda)
    - [Pip](#pip)
    - [Development version](#development-version)
  - [Usage](#usage)
    - [Command-line](#command-line)
      - [list](#list)
      - [new-service](#new-service)
      - [scratch](#scratch)
      - [Finish](#finish)
        - [clean](#clean)
        - [scratch back](#scratch-back)
        - [copy\_sftp](#copy_sftp)
      - [bioinfo\_doc](#bioinfo_doc)
      - [archive](#archive)
      - [autoclean\_sftp](#autoclean_sftp)
  - [Acknowledgements](#acknowledgements)

## Installation

### Bioconda

```bash
conda create -n buisciii-tools pip
conda activate 
conda env update --file environment.yml
```

### Pip

```bash
conda activate 
pip install .
```

### Development version

If you want to install the latest code in the repository:

```bash
conda create -n buisciii_dev pip
pip install --force-reinstall --upgrade git+https://github.com/bu-isciii/buisciii-tools.git@develop
```

## Usage

### Command-line

Run bu-isciii tools:

```bash
bu-isciii --help
```

Outputs the following:

```bash
Usage: bu-isciii [OPTIONS] COMMAND [ARGS]...

Options:
  --version                  Show the version and exit.
  -v, --verbose              Print verbose output to the console.
  -l, --log-file <filename>  Save a verbose log to a file.
  -u, --api_user TEXT        User for the API logging
  -p, --api_password TEXT    Password for the API logging
  -c, --cred_file TEXT       Config file with API logging credentials
  --help                     Show this message and exit

Commands:
  list         List available bu-isciii services.
  clean        Service cleaning.
  new-service  Create new service, it will create folder and copy...
  scratch      Copy service folder to scratch directory for execution.
  copy-sftp    Copy resolution FOLDER to sftp, change status of...
  finish       Service cleaning, remove big files, rename folders before...
  bioinfo-doc  Create the folder documentation structure in bioinfo_doc...
  archive      Archive services or retrieve services from archive
```

#### list

List available bu-isciii services:

```bash
bu-isciii list
```

Help:

```bash
Usage: bu-isciii list [OPTIONS] <service>

  List available bu-isciii services.

Options:
  --help  Show this message and exit.
```

Output:

```bash
┏━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃           Service name ┃ Description                               ┃ Github                                     ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│    assembly_annotation │ Nextflow assembly pipeline to assemble    │ https://github.com/Daniel-VM/bacass/...    │
│                        │ bacterial genomes                         │                                            │
│        mtbseq_assembly │ Mycobacterium tuberculosis mapping,       │ https://github.com/ngs-fzb/MTBseq_source   │
│                        │ variant calling and detection of          │                                            │
│                        │ resistance using MTBseq                   │                                            │
│                 mtbseq │ Mycobacterium tuberculosis mapping,       │ https://github.com/ngs-fzb/MTBseq_source   │
│                        │ variant calling and detection of          │                                            │
│                        │ resistance using MTBseq                   │                                            │
│              pikavirus │ PikaVirus, a mapping-based tool for       │ https://github.com/BU-ISCIII/PikaVirus     │
│                        │ metagenome analysis of virus.             │                                            │
│     plasmidid_assembly │ Plasmid identification tool based on      │ https://github.com/BU-ISCIII/plasmidID     │
│                        │ mapping and assisted by assembly          │                                            │
│         wgmlst_taranis │ Multilocus sequence typing (MLST) using   │ https://github.com/BU-ISCIII/taranis       │
│                        │ Taranis                                   │                                            │
│       wgmlst_chewbbaca │ Multilocus sequence typing (MLST) using   │ https://github.com/B-UMMI/chewBBACA        │
│                        │ chewBBACA                                 │                                            │
│             viralrecon │ Viral genome reconstruction analysis for  │ https://github.com/BU-ISCIII/viralrecon    │
│                        │ SARS-COV-2 data                           │                                            │
│                 rnaseq │ RNA-seq analysis                          │ https://github.com/nf-core/rnaseq          │
│          lowfreq_panel │ Low frequency variant calling from        │                                            │
│                        │ enrichment panel.                         │                                            │
│                 snippy │ Rapid haploid variant calling and core    │ https://github.com/tseemann/snippy         │
│                        │ genome alignment                          │                                            │
│       seek_and_destroy │ Simple pipeline for basic quality         │ https://github.com/GuilleGorines/Seek-Des… │
│                        │ control, host removal and exploratory     │                                            │
│                        │ analysis of samples.                      │                                            │
│ ariba_characterization │                                           │                                            │
│                mag_met │ Bioinformatics best-practise analysis     │ https://github.com/nf-core/mag             │
│                        │ pipeline for assembly, binning and        │                                            │
│                        │ annotation of metagenomes.                │                                            │
└────────────────────────┴───────────────────────────────────────────┴────────────────────────────────────────────┘
```

#### new-service

Example of usage:

```bash
bu-isciii new-service <resolution_id>
```

Help:

```bash
Usage: bu-isciii new-service [OPTIONS] <resolution id>

  Create new service, it will create folder and copy template depending on
  selected service.

Options:
  -p, --path PATH         Path to create the service folder
  -n, --no_create_folder  No create service folder, only resolution
  -a, --ask_path          Please ask for path.
  --help                  Show this message and exit.
```

#### scratch

Example of usage:

```bash
bu-isciii scratch --direction service_to_scratch <resolution_id>
```

Help:

```bash
Usage: bu-isciii scratch [OPTIONS] <resolution id>

  Copy service folder to scratch directory for execution.

Options:
  -p, --path PATH                 Absolute path to the folder containing
                                  service to copy
  -a, --ask_path                  Please ask for service path.
  -t, --tmp_dir PATH              Directory to which the files will be
                                  transfered for execution. Default:
                                  /data/bi/scratch_tmp/bi/
  -d, --direction [service_to_scratch|scratch_to_service|remove_scratch]
                                  Direction of the rsync command.
                                  service_to_scratch from /data/bi/service to
                                  /data/bi/scratch_tmp/bi/.scratch_to_service:
                                  From /data/bi/scratch_tmp/bi/ to
                                  /data/bi/service
  --help                          Show this message and exit.
```

#### Finish

Example of usage:

```bash
bu-isciii finish <resolution_id>
```

Help:

```bash
Usage: bu-isciii finish [OPTIONS] <resolution id>

  Service cleaning, remove big files, rename folders before copy and copy
  resolution FOLDER to sftp.

Options:
  -p, --path PATH         Absolute path to the folder containg the service to
                          reaname and copy
  -a, --ask_path          Please ask for path, not assume pwd.
  -s, --sftp_folder PATH  Absolute path to directory to which the files will
                          be transfered
  -t, --tmp_dir PATH      Absolute path to the scratch directory containing
                          the service.
  --help                  Show this message and exit.
```

Finish module performs de following modules at onin this order, at once:

##### clean

Example of usage:

```bash
bu-isciii clean <resolution_id>
```

Help:

```bash
Usage: bu-isciii clean [OPTIONS] <resolution id>

  Service cleaning. It will either remove big files, rename folders before
  copy, revert this renaming, show removable files or show folders for no
  copy.

Options:
  -p, --path PATH                 Absolute path to the folder containing
                                  service to clean
  -a, --ask_path                  Please ask for path
  -s, --option [full_clean|rename_nocopy|clean|revert_renaming|show_removable|show_nocopy]
                                  Select what to do inside the cleanning step:
                                  full_clean: delete files and folders to
                                  clean, rename no copy and deleted folders,
                                  rename_nocopy: just rename no copy folders,
                                  clean: delete files and folders to
                                  clean,revert_renaming: remove no_copy and
                                  delete tags,show_removable: list folders and
                                  files to remove and show_nocopy: show
                                  folders to rename with no_copy tag.
  --help                          Show this message and exit.
```

##### scratch back

```bash
bu-isciii scratch --direction scratch_to_service <resolution_id>
```

##### copy_sftp

Example of usage:

```bash
bu-isciii copy-sftp <resolution_id>
```

Help:

```bash
Usage: bu-isciii copy-sftp [OPTIONS] <resolution id>

  Copy resolution FOLDER to sftp, change status of resolution in iskylims and
  generate md, pdf, html.

Options:
  -p, --path PATH         Absolute path to directory containing files to
                          transfer
  -a, --ask_path          Please ask for path
  -s, --sftp_folder PATH  Absolute path to directory to which the files will
                          be transfered
  --help                  Show this message and exit.
```

#### bioinfo_doc

Example of usage:

```bash
bu-isciii bioinfo-doc <resolution_id>
```

Help:

```bash
Usage: bu-isciii bioinfo-doc [OPTIONS] <resolution id>

  Create the folder documentation structure in bioinfo_doc server

Options:
  -p, --path PATH                 Absolute path to bioinfo_doc directory.
  -a, --ask_path                  Please ask for path, not assume
                                  /data/bioinfo_doc/.
  -t, --type [service_info|delivery]
                                  Select the documentation that will generate
  -s, --sftp_folder PATH          Absolute path to sftp folfer containing
                                  service folder
  -r, --report_md PATH            Absolute path to markdown report to use
                                  instead of the one in config file
  -m, --results_md PATH           Absolute path to markdown report to use
                                  instead of the one in config file
  -e, --email_psswd TEXT          Password for bioinformatica@isciii.es
  --help                          Show this message and exit.
```

#### archive

Example of usage:

```bash
bu-isciii archive --date_from 2022-01-01 --date_until 2023-01-01
```

Help:

```bash
Usage: bu-isciii archive [OPTIONS]

  Archive services or retrieve services from archive

Options:
  -s, --service_id TEXT           service id, pe SRVCNM787
  -sf, --service_file TEXT        file with services ids, one per line
  -t, --ser_type [services_and_colaborations|research]
                                  Select which folder you want to archive.
  -o, --option [archive|retrieve_from_archive]
                                  Select either you want to archive services
                                  or retrieve a service from archive.
  -sp, --skip_prompts             Avoid prompts (except on service choosing)
  -df, --date_from TEXT           The date from which start search (format
                                  'YYYY-MM-DD')
  -du, --date_until TEXT          The date from which end search (format
                                  'YYYY-MM-DD')
  -f, --output_name TEXT          Tsv output path + filename with archive
                                  stats and info
  --help                          Show this message and exit.
```

#### autoclean_sftp

Example of usage:

```bash
bu-isciii autoclean-sftp
```

Help:

```bash
Usage: bu-isciii autoclean-sftp [OPTIONS]

  Clean old sftp services

Options:
  -s, --sftp_folder PATH  Absolute path to sftp folder
  -d, --days INTEGER      Integer, remove files older than a window of `-d
                          [int]` days. Default 14 days.
  --help                  Show this message and exit.
```

## Acknowledgements

Python package idea and design is really inspired in [nf-core/tools](https://github.com/nf-core/tools).
