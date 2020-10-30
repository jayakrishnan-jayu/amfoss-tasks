package main

import (
	"context"
	"fmt"
	"github.com/vartanbeno/go-reddit/reddit"
)

var ctx = context.Background()

func main() {
	withCredentials := reddit.WithCredentials("id", "secret", "username", "password")
	client, _ := reddit.NewClient(withCredentials)
	subReddit, _, err := client.Subreddit.NewPosts(ctx, "memes",&reddit.ListOptions{
					Limit: 10,
	})


	if err != nil {
		fmt.Println(err)
		return
	} 

	for i, post := range subReddit {
		fmt.Print(i+1)
		fmt.Println(" Upvoting " + post.Title + " with id " + post.FullID)
		_, error := client.Post.Upvote(ctx, post.FullID)
		if error != nil {
			fmt.Println(error)
			return
		}
	}
	 
	
	
}