# cat train2 >> train

# # LEVEL 1
# echo "LEVEL 1 Training"
# python giveFeatures.py train trainWithFeatures Train
# crf_learn template_file trainWithFeatures model
# python giveFeatures.py train_withoutLabels testWithFeatures Test
# crf_test -m model testWithFeatures > test_result1

# # LEVEL 2
# echo "LEVEL 2 Training"
# python addLabels.py test_result1 train train4
# crf_learn template_file2 train4 model2

# TESTINGS LEVEL1
# echo "LEVEL 1 Testing"
python giveFeatures.py $1 testWithFeatures Test
crf_test -m model testWithFeatures > test_result

# echo "LEVEL 2 Testing"
crf_test -m model2 test_result > test_result2
python changeFormat.py test_result2 > $2
#python Fscore_ner.py $2 test_gold 2> Error_Analysis

# subl Error_Analysis