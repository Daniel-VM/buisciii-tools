echo -e "sample_ID\tTotalReads\tMappedReads\tFlu_type\tReads_HA\tReads_MP\tReads_NA\tReads_NP\tReads_NS\tReads_PA\tReads_PB1\tReads_PB2" > irma_stats.txt; cat ../samples_id.txt | while read in; do paste <(echo ${in}) <(grep '1-initial' ${in}/tables/READ_COUNTS.txt | cut -f2) <(grep '3-match' ${in}/tables/READ_COUNTS.txt | cut -f2) <(paste <(grep '4-[A-B]_HA' ${in}/tables/READ_COUNTS.txt | cut -f1 | cut -d '_' -f1,3 | cut -d '-' -f2) <(grep '4-[A-B]_NA' ${in}/tables/READ_COUNTS.txt | cut -f1 | cut -d '_' -f3) | tr '\t' '_') <(grep '4-[A-B]_HA' ${in}/tables/READ_COUNTS.txt | cut -f2) <(grep '4-[A-B]_MP' ${in}/tables/READ_COUNTS.txt | cut -f2) <(grep '4-[A-B]_NA' ${in}/tables/READ_COUNTS.txt | cut -f2) <(grep '4-[A-B]_NP' ${in}/tables/READ_COUNTS.txt | cut -f2) <(grep '4-[A-B]_NS' ${in}/tables/READ_COUNTS.txt | cut -f2) <(grep '4-[A-B]_PA' ${in}/tables/READ_COUNTS.txt | cut -f2) <(grep '4-[A-B]_PB1' ${in}/tables/READ_COUNTS.txt | cut -f2) <(grep '4-[A-B]_PB2' ${in}/tables/READ_COUNTS.txt | cut -f2); done >> irma_stats.txt