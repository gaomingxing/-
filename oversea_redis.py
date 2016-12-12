#coding:utf-8
#name:oversea_redis.py

import redis


redis_conn_0 = redis.StrictRedis.from_url("redis://:Zhxg-2016@47.88.33.29:6379/0")
redis_conn_9 = redis.StrictRedis.from_url("redis://:Zhxg-2016@47.88.33.29:6379/9")

def staticstic_0(box):
    print '0 db:'
    for key in box:
        print key, redis_conn_0.llen(key)

def staticstic_9(box):
    print '9 db:'
    for key in box:
        print key, redis_conn_9.zcard(key)

if __name__ == '__main__':
    weekly2 = ('quixey_hulu_movie_all_wdc', 'quixey_us_youtobe_all', 'custom_data_crackle', 'custom_data_hulu_tvshow', 'custom_data_quixey_vividseats_test', "fox.com")
    weekly2_9 = ('zset_hulu_success_urls_wdc', 'zset_youtube_success_urls', 'crackle_show_success_url', 'hulu_show_success_url', 'zset_vividseats_success_urls')
    weekly3 = ('quixey_us_eventbrite_all_new', 'quixey_us_hotstar_test', 'quixey_us_flipkart_test', 'vevo.com', 'custom_data_quixey_saavn_test', 'expedia.com', 'quixey_us_vimeo_test', 'quixey_us_songkick_test', 'custom_data_quixey_netflix_test', 'custom_data_quixey_macys_test', 'custom_data_booking_all')
    weekly3_9 = ('zset_eventbrite_succeed_urls', 'zset_hotstar_succeed_url', 'zset_flipkart_succeed_url', 'vevo_success_url', 'zset_saavn_success_urls', 'zset_expedia_success', 'zset_vimeo_succeed_url', 'zset_songkick_succeed_url', 'zset_netflix_success_urls', 'zset_macys_success_urls', 'zset_booking_succeed_url')
    weekly4 = ('quixey_us_hichao_test',)
    weekly4_9 = ('zset_hichao_succeed_url',)
    monthly = ('quixey_us_snapdeal_test', 'custom_data_magic', 'custom_data_us_all_shopclues')
    monthly_9 = ('zset_snapdeal_succeed_urls', 'zset_magicbricks_success_urls')

    print 'weekly2'
    staticstic_0(weekly2)
    staticstic_9(weekly2_9)

    print '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
    print 'weekly3'
    staticstic_0(weekly3)
    staticstic_9(weekly3_9)

    print '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
    print 'weekly4'
    staticstic_0(weekly4)
    staticstic_9(weekly4_9)

    print '^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'
    print 'monthly'
    staticstic_0(monthly)
    staticstic_9(monthly_9)

