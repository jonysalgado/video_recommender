# video_recommender


### Code used to get labelling on label studio

<View>
  <View style="padding: 25px;                box-shadow: 2px 2px 8px #AAA">
    <Header value="$title"/>
    <Image name="image" value="$thumbnails"/>
  </View>
  <View style="padding: 25px;                box-shadow: 2px 2px 8px #AAA">
    <Text name="description" value="$description" granularity="word" highlightColor="#ff0000"/>
  </View>
  <Text name="view_count" value="$view_count" granularity="word" highlightColor="#ff0000"/>
  <Text name="uploader" value="$uploader" granularity="word" highlightColor="#ff0000"/>
  <Choices name="intent" toName="image" choice="single" showInLine="true">
    <Choice value="É interessante"/>
    <Choice value="Não é interessante"/>
  </Choices>
</View>


# Run Flask

set FLASK_APP=app
flask run