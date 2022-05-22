from deepsegment import DeepSegment
segmenter = DeepSegment('en', checkpoint_name='finetuned_model_name')
segmenter.segment('I am Batman i live in gotham')