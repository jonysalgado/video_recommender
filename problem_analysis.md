## Qual é o problema?

Tempo gasto buscando vídeos no youtube

## Qual a solução ideal?

Ter uma lista com apenas os vídeos que eu, com certeza, irei gostar.

## Como eu posso fazer isso com Data Science/ML?

Criar uma solução de recomendação de vídeos

## Como essa solução será usada em produção?

Abordagem com "ponto de corte" -> retornar apenas Top 3
Abordagem de ranking -> ordene os vídeos mais interessantes primeiro

Web app com os vídeos (links) e as previsões ordenadas

## Como eu vou saber que deu certo?

Métrica primária: quantos vídeos dentro os top N recomendados eu assisti até o final. 
Os top N recomendados são mais assistidos do que os top N da busca do youtube?

## Como eu vou saber que deu certo?

Métrica primária: dos top N vídeos, quantos eu coloco na lista do watch later.

## Gerar playlist

Para gerar playlist basta fazer http://www.youtube.com/watch_videos?video_ids=J6PBD-
  wNEDs,afwPe_OqPX0,OGcG4jSKOVA,hegL0V4ckco,LajAWn51HmE

Colocar os IDs dos vídeos na lista de IDs


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