import tweepy as tp
import credentials as dta
import scrape2 as sc
from datetime import date

auth = tp.OAuth1UserHandler(consumer_key=dta.API_Key, consumer_secret=dta.API_Key_Secret)   
auth.set_access_token(dta.access_token,dta.access_token_secret)
API=tp.API(auth,retry_delay=2,retry_count=2)

def Fashion(name="Fashion"):        
    fashion_keywords=["#clothes" ,"#clothing" ,"#clothingbrand", "#clothingstyle","necklace bracelets","#design","#fashion" ,"#fashionstyle","#instafashion" ,"#lifestyle" ,"#mensfashion" ,"#streetwear" ,"#style" ,"#tshirt","#Jackets"]
    fashion_tweet=[]
    count=0
    for fashion in fashion_keywords:
        tweets_fashion = tp.Cursor(API.search_tweets,fashion,tweet_mode='extended', lang='en',include_entities=True).items(70)
        tweet_count=0
        for tweet in tweets_fashion:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                flag=0 
                flag1=0
                hashtxt=[]
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    for h in hashtag:
                        hashtxt.append(h['text'])
                    flag=0 
                    flag1=0
                    if 'media' in tweet.entities:
                        for image in  tweet.entities['media'][0]:
                            line={'Category':f"{name}",'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                        print("Image found!")
                        flag=1
                    else:
                        line={'Category':f"{name}",'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}
                
                # Access video info
                try:
                    if 'media' in tweet.entities:
                        for media in tweet.extended_entities['media']:
                            line['video_img_url']=media['media_url']
                        flag1=1
                except:
                    pass
                line['id']=id
            except Exception as e:
                print(str(e))
            except StopIteration:
                print("Error occured !!")
                break
            try:
                if trend_score>=2:
                    fashion_tweet.append(line)
                else:
                    print("Tweet rejected since very less popular")
            except:
                fashion_tweet.append(line)
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets scraped :=> {count}")
    fashion_tweet=sc.remove_duplicates(fashion_tweet)
    new_fashion_tweet=sc.sort__(fashion_tweet,'trend_score')

    img_url=sc.get_img_url(new_fashion_tweet)
    for url in img_url:
        for i,k in url.items():
            sc.download_img(k,f"{i}.jpeg",f"{name}")
    sc.write_json_file(new_fashion_tweet,f"{name}")


def electronics(name="Electronics"):
    Electronics_keywords=["phones","#computers","#android","#tech","#innovation","laptops"," #Technology","#iPhone14"]
    Electronics_tweet=[]
    count=0
    for electronic in Electronics_keywords:
        tweets_electronics = tp.Cursor(API.search_tweets,electronic,tweet_mode='extended', lang='en',include_entities=True).items(70)
        tweet_count=0
        for tweet in tweets_electronics:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                # url=tweet.urls
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                hashtxt=[]
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    for h in hashtag:
                        hashtxt.append(h['text'])
                if 'media' in tweet.entities:
                    for image in  tweet.entities['media'][0]:
                        line={'Category':f"{name}",'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}

                    print("Image found!")
                else:
                    line={'Category':f"{name}",'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}

                # Access video info
                try:
                    if 'media' in tweet.entities:
                        for media in tweet.extended_entities['media']:
                            line['video_img_url']=media['media_url']
                except:
                    pass
                line['id']=id
            except Exception as e:
                print(str(e))
            except StopIteration:
                break     
            try:
                if trend_score >=2:
                    Electronics_tweet.append(line)
                else:
                    print("Tweet rejected since very less popular")
            except:
                Electronics_tweet.append(line)
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets scraped :=> {count}")
    Electronics_tweet=sc.remove_duplicates(Electronics_tweet)
    new_Electronics_tweet=sc.sort__(Electronics_tweet,'trend_score')
    img_url=sc.get_img_url(Electronics_tweet)
    for url in img_url:
        for i,k in url.items():
            sc.download_img(k,f"{i}.jpeg",f"{name}")
    sc.write_json_file(new_Electronics_tweet,f"{name}")



def home_Funiture(name='Home_And_Furniture'):
    Home_Funiture_keywords=["#wallpaper","#flowers","#summer","#homedecor","#luxury","furniture","Dinnerware","#lamps","#coffee","#mugs","#giftideas","home design"]
    Home_Funiture_tweet=[]
    count=0
    for Home_Funiture in Home_Funiture_keywords:
        tweets_Home_Funiture = tp.Cursor(API.search_tweets,Home_Funiture,tweet_mode='extended',lang='en',include_entities=True).items(70)
        tweet_count=0
        for tweet in tweets_Home_Funiture:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                flag1=0
                flag=0
                hashtxt=[]
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    for h in hashtag:
                        hashtxt.append(h['text'])

                if 'media' in tweet.entities:
                    for image in  tweet.entities['media'][0]:
                        line={'Category':f"{name}",'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                    print("Image found!")
                    
                else:
                    line={'Category':f"{name}",'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}
                
                # Access video info
                try:
                    if 'media' in tweet.entities:
                        for media in tweet.extended_entities['media']:
                            line['video_img_url']=media['media_url']
                      
                except:
                    pass
                line['id']=id
            except StopIteration:
                break     
            try:
                if trend_score >=2:
                    Home_Funiture_tweet.append(line)
                    
                else:
                    print("Tweet rejected since very less popular")    
            except:
                Home_Funiture_tweet.append(line)
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets scraped :=> {count}")
    Home_Funiture_tweet=sc.remove_duplicates(Home_Funiture_tweet)
    new_Home_Funiture_tweet=sc.sort__(Home_Funiture_tweet,'trend_score')
    img_url=sc.get_img_url(Home_Funiture_tweet)
    for url in img_url:
        for i,k in url.items():
            sc.download_img(k,f"{i}.jpeg",f"{name}")
    sc.write_json_file(new_Home_Funiture_tweet,f"{name}")

def sports_More(name='Sports_And_MoRE'):
    Sports_More_keywords=["#Sports","#fitness","#yoga","#gym","#weightloss","#tennis","#cricket","#badminton","batsman","#shuttles","football","#skateboard","#athlete","#Hockey","#skate","#tent","#hiking","#pool","#swimwear","#swim"]
    Sports_More_tweet=[]
    count=0
    for Sports_More in Sports_More_keywords:
        tweets_Sports_More = tp.Cursor(API.search_tweets,Sports_More,tweet_mode='extended',lang='en',include_entities=True).items(50)
        tweet_count=0
        for tweet in tweets_Sports_More:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                hashtxt=[]
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    for h in hashtag:
                        hashtxt.append(h['text'])
                if 'media' in tweet.entities:
                    for image in  tweet.entities['media'][0]:
                        line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                    print("Image found!")
                    flag=1
                else:
                    line={'Category':f"{name}",'tweet_id':id,'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}

                # Access video info
                try:
                    if 'media' in tweet.entities:
                        for media in tweet.extended_entities['media']:
                            line['video_img_url']=media['media_url']
                        flag1=1
                except:
                    pass
                line['id']=id
            except Exception as e:
                print(str(e))
            except StopIteration:
                break     
            if trend_score >=2:
                Sports_More_tweet.append(line)
            else:
                print("Tweet rejected since very less popular")
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets scraped :=> {count}")
    Sports_More_tweet=sc.remove_duplicates(Sports_More_tweet)
    new_Sports_More_tweet=sc.sort__(Sports_More_tweet,'trend_score')
    img_url=sc.get_img_url(Sports_More_tweet)
    for url in img_url:
        for i,k in url.items():
            sc.download_img(k,f"{i}.jpeg",f"{name}")
    sc.write_json_file(new_Sports_More_tweet,f"{name}")

def kids_Babies(name="Kids_And_toys"):
    kids_babies_keywords=["#cutebaby","Lego","#toys","#games","#Marvel","#kids","#kindergarden","#Backpack","#childrenstoys","#toysforboys","#toys4life" ]
    kids_babies_tweet=[]
    count=0
    for kids_babies in kids_babies_keywords:
        tweets_kids_babies = tp.Cursor(API.search_tweets,kids_babies,tweet_mode='extended', lang='en',include_entities=True).items(70)
        tweet_count=0
        for tweet in tweets_kids_babies:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                # url=tweet.urls
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                hashtxt=[]
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    for h in hashtag:
                        hashtxt.append(h['text'])    
                if 'media' in tweet.entities:
                    for image in  tweet.entities['media'][0]:
                        line={'Category':f"{name}",'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                    print("Image found!")
                    flag=1
                else:
                    line={'Category':f"{name}",'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}
               
                                # Access video info
                try:
                    if 'media' in tweet.entities:
                        for media in tweet.extended_entities['media']:
                            line['video_img_url']=media['media_url']
                except:
                    pass
                line['id']=id
            except Exception as e:
                print(str(e))
            except StopIteration:
                break     
            if trend_score>=2:
                kids_babies_tweet.append(line)
            else:
                print("Tweet rejected since very less popular")
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets scraped :=> {count}")
    kids_babies_tweet=sc.remove_duplicates(kids_babies_tweet)
    new_kids_babies_tweet=sc.sort__(kids_babies_tweet,'trend_score')
    img_url=sc.get_img_url(kids_babies_tweet)
    for url in img_url:
        for i,k in url.items():
            sc.download_img(k,f"{i}.jpeg",f"{name}")
    sc.write_json_file(new_kids_babies_tweet,f"{name}")

def beauTy(name="Skincare_And_Beauty"):
    beauty_keywords=["#makeup","#glamour","#cosmetics","#lips","#eyeshadow","#skincare","#cosmetics","#instamakeup","#ethicalmakeup","#skincare","#skincareroutine"]
    beauty_tweet=[]
    count=0

    for beauty in beauty_keywords:
        tweets_beauty = tp.Cursor(API.search_tweets,beauty,tweet_mode='extended', lang='en',include_entities=True).items(70)
        tweet_count=0
        for tweet in tweets_beauty:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                flag=0;flag1=0
                hashtxt=[]
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    for h in hashtag:
                        hashtxt.append(h['text'])  
                if 'media' in tweet.entities:
                    for image in  tweet.entities['media'][0]:
                        line={'Category':f"{name}",'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                    print("Image found!")
                    flag=1
                else:
                    line=line={'Category':f"{name}",'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}
                
                                # Access video info
                try:
                    # if image in tweet.extended_entities['media']:
                    #         tweet_media=tweet.extended_entities["media"][0]["video_info"]["variants"][0]["url"]
                    #         line['video_url']=tweet_media
                    if 'media' in tweet.entities:
                        for media in tweet.extended_entities['media']:
                            line['video_img_url']=media['media_url']
                        flag1=1
                except:
                    pass
                line['id']=id
            except Exception as e:
                print(str(e))
            except StopIteration:
                break  
            if trend_score>=2:
                beauty_tweet.append(line)
            else:
                print("Tweet rejected since very less popular")
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets scraped :=> {count}")
    beauty_tweet=sc.remove_duplicates(beauty_tweet)
    new_beauty_tweet=sc.sort__(beauty_tweet,'trend_score')
    img_url=sc.get_img_url(beauty_tweet)
    for url in img_url:
        for i,k in url.items():
            sc.download_img(k,f"{i}.jpeg",f"{name}")
    sc.write_json_file(new_beauty_tweet,f"{name}")

def books_Stationaries(name="Books_AND_Stationaries"):
    books_stationaries_keywords=["book","books","#BookTwitter","#amreading","#Kindle","#books","notebook","#Statistics","#Coding","#Programming","#comics","#craftsforchildren"]
    books_stationaries_tweet=[]
    count=0
    for books_stationaries in books_stationaries_keywords:
        tweets_books_stationaries = tp.Cursor(API.search_tweets,books_stationaries,tweet_mode='extended',lang='en',include_entities=True).items(70)
        tweet_count=0
        for tweet in tweets_books_stationaries:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                hashtxt=[]
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    for h in hashtag:
                        hashtxt.append(h['text'])
                if 'media' in tweet.entities:
                    for image in  tweet.entities['media'][0]:
                        line={'Category':f"{name}",'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                    print("Image found!")
                else:
                    line=line={'Category':f"{name}",'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}

                # Access video info
                try:
                    if 'media' in tweet.entities:
                        for media in tweet.extended_entities['media']:
                            line['video_img_url']=media['media_url']
                       
                except:
                    pass
                line['id']=id
            except Exception as e:
                print(str(e))
            except StopIteration:
                break     
            if trend_score>=2:
                books_stationaries_tweet.append(line)
            else:
                print("Tweet rejected since very less popular")
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets scraped :=> {count}")
    books_stationaries_tweet=sc.remove_duplicates(books_stationaries_tweet)
    new_books_stationaries_tweet=sc.sort__(books_stationaries_tweet,'trend_score')
    img_url=sc.get_img_url(books_stationaries_tweet)
    for url in img_url:
        for i,k in url.items():
            sc.download_img(k,f"{i}.jpeg",f"{name}")
    sc.write_json_file(new_books_stationaries_tweet,f"{name}")


def top_trends(name='Top_Trends'):
    trend_result=API.get_place_trends(dta.i_woeid)
    list=[]
    try:
        for trend in trend_result[0]["trends"]:
            a= trend['name']
            # write_json(trends)
            list.append(a)
    except:                                          
        print("Somethng went wrong")
    trending_keywords=list
    trending_tweet=[]
    count=0
    for tre in trending_keywords:
        tweets_ = tp.Cursor(API.search_tweets,tre,tweet_mode='extended', result_type="recent",lang='en',include_entities=True).items(15)
        tweet_count=0
        for tweet in tweets_:
            try:
                txt=tweet.full_text
                id=tweet.id
                url="https://twitter.com/twitter/statuses/"+str(id)
                likes=tweet.favorite_count
                retweet_count=tweet.retweet_count
                trend_score=likes+retweet_count
                if 'hashtags' in tweet.entities:
                    hashtag=tweet.entities['hashtags']
                    hashtxt=[]
                    for h in hashtag:
                        hashtxt.append(h['text'])
                    
                if 'media' in tweet.entities:
                    for image in  tweet.entities['media'][0]:
                        line={'Category':f"{name}",'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':tweet.entities["media"][0]['media_url'],'hashtags_text':hashtxt}
                    print("Image found!")
                else:
                    line=line={'Category':f"{name}",'url':url,'text':txt,'trend_score':trend_score,'IMAGE_URL':"null",'hashtags_text':hashtxt}

                
                # Access video info
                                # Access video info
                try:
                    # if image in tweet.extended_entities['media']:
                    #         tweet_media=tweet.extended_entities["media"][0]["video_info"]["variants"][0]["url"]
                    #         line['video_url']=tweet_media
                    if 'media' in tweet.entities:
                        for media in tweet.extended_entities['media']:
                            line['video_img_url']=media['media_url']
                        
                except:
                    pass
                line['id']=id
            except Exception as e:
                print(str(e))
            except StopIteration:
                break     
            if trend_score>=2:
                trending_tweet.append(line)
            else:
                print("Tweet rejected since very less popular")
            tweet_count+=1
        count=count+tweet_count
        print(count)
    print(f"The total tweets scraped:=> {count}")
    trending_tweet=sc.remove_duplicates(trending_tweet)
    new__tweet=sc.sort__(trending_tweet,'trend_score')
    img_url=sc.get_img_url(trending_tweet)
    for url in img_url:
        for i,k in url.items():
            sc.download_img(k,f"{i}.jpeg",f"{name}")
    sc.write_json_file(new__tweet,f"{name}")
