{"{$itemUrl|default:'https://purple.com'}?utm_medium=SMS&utm_source=cordial&utm_content=bulk&utm_term=rt&utm_campaign={$message.name|replace:' ':'_'}&mcid={$mcID}&linkid={$linkID}"|shorten:6}

{"{$bestMatchLink|default:'https://purple.com'}?utm_medium=SMS&utm_source=cordial&utm_content=bulk&utm_term=rt&utm_campaign={$message.name|replace:' ':'_'}&mcid={$mcID}&linkid={$linkID}"|shorten:6}


{strip}
{include 'content:mattress_browse_mms_logic' scope='parent' assign='blackhole'}
{$imageUrl = $data.displayItem.ab_product_image_1|default:'https://images.cordial.com/927/347x435/Restore_25.png'}
{$utils->setMmsMedia($imageUrl,"image")}
{$itemUrl = $data.displayItem.url|default:'https://purple.com'}

{/strip}PURPLE: Want better sleep? You're in the right place.
That mattress you browsed is $300 off + save $200 more on a base → 

{"{$itemUrl|default:'https://purple.com'}?utm_medium=SMS&utm_source=cordial&utm_content=bulk&utm_term=rt&utm_campaign={$message.name|replace:' ':'_'}&mcid={$mcID}&linkid={$linkID}"|shorten:6}
