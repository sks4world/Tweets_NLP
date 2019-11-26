import pandas as pd
import os

def get_sample_data(file_path):
	print('get_sample_data')
	df = pd.read_csv('Tweets_zika_FollowerHash_usedforSampling_Nov25_1.csv')
	#print(df.count())
	#df_threat_min = df.sort_values('threat').filter(['threat','protect', 'fear', 'pain', 'retweets', 'Followercount', 'hashtags']).loc[0:49]
	df_threat_min = df.sort_values('threat').filter(['corpus_tweets', 'Tweets', 'threat','protect', 'fear', 'pain', 'retweets', 'Followercount', 'hashtags']).head(50)
	#print(df_threat_min.shape)
	#print(df_threat_min.head(10))
	df_threat_max = df.sort_values('threat', ascending=False).filter(['corpus_tweets', 'Tweets', 'threat','protect', 'fear', 'pain', 'retweets', 'Followercount', 'hashtags']).head(50)
	df_threat = pd.concat([df_threat_min, df_threat_max])
	df_threat_min.to_csv('Factors_Influencing_Zika_Retweets_Sample_tweets_3.csv')
	df_threat_max.to_csv('Factors_Influencing_Zika_Retweets_Sample_tweets_4.csv')
	df_threat.to_csv('Factors_Influencing_Zika_Retweets_Sample_tweets_5.csv')

	#Protect
	df_protect_min = df.sort_values('protect').filter(['corpus_tweets', 'Tweets', 'threat','protect', 'fear', 'pain', 'retweets', 'Followercount', 'hashtags']).head(50)
	df_protect_max = df.sort_values('protect', ascending=False).filter(['corpus_tweets', 'Tweets', 'threat','protect', 'fear', 'pain', 'retweets', 'Followercount', 'hashtags']).head(50)

	#pain
	df_pain_min = df.sort_values('pain').filter(['corpus_tweets', 'Tweets', 'threat','protect', 'fear', 'pain', 'retweets', 'Followercount', 'hashtags']).head(50)
	df_pain_max = df.sort_values('pain', ascending=False).filter(['corpus_tweets', 'Tweets', 'threat','protect', 'fear', 'pain', 'retweets', 'Followercount', 'hashtags']).head(50)

	#fear
	df_fear_min = df.sort_values('fear').filter(['corpus_tweets', 'Tweets', 'threat','protect', 'fear', 'pain', 'retweets', 'Followercount', 'hashtags']).head(50)
	df_fear_max = df.sort_values('fear', ascending=False).filter(['corpus_tweets', 'Tweets', 'threat','protect', 'fear', 'pain', 'retweets', 'Followercount', 'hashtags']).head(50)

	#Output
	df_samples = pd.concat([df_threat_min, df_threat_max,df_protect_min,df_protect_max,df_pain_min,df_pain_max,df_fear_min,df_fear_max])
	#df_samples.to_csv('Factors_Influencing_Zika_Retweets_Sample_tweets_6.csv')
	print(df_samples.describe())
	df_samples['threat'] = df_samples['threat'].apply(lambda x: 1 if x > 1 else x)
	df_samples['protect'] = df_samples['protect'].apply(lambda x: 1 if x > 1 else x)
	df_samples['fear'] = df_samples['fear'].apply(lambda x: 1 if x > 1 else x)
	df_samples['pain'] = df_samples['pain'].apply(lambda x: 1 if x > 1 else x)
	df_samples.to_csv('Factors_Influencing_Zika_Retweets_Sample_tweets_7.csv')
	print(df_samples.describe())



def set_file_path():
	print('set_file_path')
	os.chdir('give your file_path')

def main():
	print('main')
	file_path=set_file_path()
	get_sample_data(file_path)

main()
