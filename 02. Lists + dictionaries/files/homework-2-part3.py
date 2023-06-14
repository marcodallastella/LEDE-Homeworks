# Marco Dalla Stella
# 2023-06-07
# Homework 2, Part 3

import json

data = json.loads("{\"tracks\":[{\"album\":{\"album_type\":\"single\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/1YxmW7DO2dM05gwMKTbr7l\"},\"href\":\"https://api.spotify.com/v1/albums/1YxmW7DO2dM05gwMKTbr7l\",\"id\":\"1YxmW7DO2dM05gwMKTbr7l\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/5b14b24dea78b0a14244ccb86f3bfd20bf77326d\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/177939e6656bd0ae46d12e1f36e9162016d28a3c\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/7b42b976267520f4dbb2f67e1baa63ca13bdbfdb\",\"width\":64}],\"name\":\"Fake Love\",\"type\":\"album\",\"uri\":\"spotify:album:1YxmW7DO2dM05gwMKTbr7l\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":207813,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600333\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/6NMNgWgEAzde5M8U3lc6FN\"},\"href\":\"https://api.spotify.com/v1/tracks/6NMNgWgEAzde5M8U3lc6FN\",\"id\":\"6NMNgWgEAzde5M8U3lc6FN\",\"name\":\"Fake Love\",\"popularity\":90,\"preview_url\":\"https://p.scdn.co/mp3-preview/b1c79b52128cc45a962cb87ba5a616ea6a435356?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:6NMNgWgEAzde5M8U3lc6FN\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3tVQdUvClmAT7URs9V3rsp\"},\"href\":\"https://api.spotify.com/v1/artists/3tVQdUvClmAT7URs9V3rsp\",\"id\":\"3tVQdUvClmAT7URs9V3rsp\",\"name\":\"WizKid\",\"type\":\"artist\",\"uri\":\"spotify:artist:3tVQdUvClmAT7URs9V3rsp\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/77DAFfvm3O9zT5dIoG0eIO\"},\"href\":\"https://api.spotify.com/v1/artists/77DAFfvm3O9zT5dIoG0eIO\",\"id\":\"77DAFfvm3O9zT5dIoG0eIO\",\"name\":\"Kyla\",\"type\":\"artist\",\"uri\":\"spotify:artist:77DAFfvm3O9zT5dIoG0eIO\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":173986,\"explicit\":false,\"external_ids\":{\"isrc\":\"USCM51600028\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/12VWzyPDBCc8fqeWCAfNwR\"},\"href\":\"https://api.spotify.com/v1/tracks/12VWzyPDBCc8fqeWCAfNwR\",\"id\":\"12VWzyPDBCc8fqeWCAfNwR\",\"name\":\"One Dance\",\"popularity\":84,\"preview_url\":\"https://p.scdn.co/mp3-preview/98f60b086bb1da2ca2e4c217331b8c8cc801358d?cid=null\",\"track_number\":12,\"type\":\"track\",\"uri\":\"spotify:track:12VWzyPDBCc8fqeWCAfNwR\"},{\"album\":{\"album_type\":\"single\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/2z3NlPY0n0gHJPCPqrzA6V\"},\"href\":\"https://api.spotify.com/v1/albums/2z3NlPY0n0gHJPCPqrzA6V\",\"id\":\"2z3NlPY0n0gHJPCPqrzA6V\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/5b14b24dea78b0a14244ccb86f3bfd20bf77326d\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/177939e6656bd0ae46d12e1f36e9162016d28a3c\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/7b42b976267520f4dbb2f67e1baa63ca13bdbfdb\",\"width\":64}],\"name\":\"Sneakin’\",\"type\":\"album\",\"uri\":\"spotify:album:2z3NlPY0n0gHJPCPqrzA6V\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/1URnnhqYAYcrqrcwql10ft\"},\"href\":\"https://api.spotify.com/v1/artists/1URnnhqYAYcrqrcwql10ft\",\"id\":\"1URnnhqYAYcrqrcwql10ft\",\"name\":\"21 Savage\",\"type\":\"artist\",\"uri\":\"spotify:artist:1URnnhqYAYcrqrcwql10ft\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":251333,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600337\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/4ckuS4Nj4FZ7i3Def3Br8W\"},\"href\":\"https://api.spotify.com/v1/tracks/4ckuS4Nj4FZ7i3Def3Br8W\",\"id\":\"4ckuS4Nj4FZ7i3Def3Br8W\",\"name\":\"Sneakin’\",\"popularity\":82,\"preview_url\":\"https://p.scdn.co/mp3-preview/4fa89ace286252c33a1ca0d36e7555d6a451a2db?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:4ckuS4Nj4FZ7i3Def3Br8W\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/5pKCCKE2ajJHZ9KAiaK11H\"},\"href\":\"https://api.spotify.com/v1/artists/5pKCCKE2ajJHZ9KAiaK11H\",\"id\":\"5pKCCKE2ajJHZ9KAiaK11H\",\"name\":\"Rihanna\",\"type\":\"artist\",\"uri\":\"spotify:artist:5pKCCKE2ajJHZ9KAiaK11H\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":263373,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600088\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/7fJtPlEZKxu6gvkfBFc5tW\"},\"href\":\"https://api.spotify.com/v1/tracks/7fJtPlEZKxu6gvkfBFc5tW\",\"id\":\"7fJtPlEZKxu6gvkfBFc5tW\",\"name\":\"Too Good\",\"popularity\":79,\"preview_url\":\"https://p.scdn.co/mp3-preview/e702c76de627c3fb04da1bcbf6a8b53c3326a0cc?cid=null\",\"track_number\":16,\"type\":\"track\",\"uri\":\"spotify:track:7fJtPlEZKxu6gvkfBFc5tW\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":245226,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600080\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/4CpKEkdGbOJV51cSvx7SoG\"},\"href\":\"https://api.spotify.com/v1/tracks/4CpKEkdGbOJV51cSvx7SoG\",\"id\":\"4CpKEkdGbOJV51cSvx7SoG\",\"name\":\"Controlla\",\"popularity\":79,\"preview_url\":\"https://p.scdn.co/mp3-preview/c5b5845dc83410f5731e395c5a725d6b6e94ff69?cid=null\",\"track_number\":11,\"type\":\"track\",\"uri\":\"spotify:track:4CpKEkdGbOJV51cSvx7SoG\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3ubFn9991d8ygM3MSi7NDi\"},\"href\":\"https://api.spotify.com/v1/artists/3ubFn9991d8ygM3MSi7NDi\",\"id\":\"3ubFn9991d8ygM3MSi7NDi\",\"name\":\"Future\",\"type\":\"artist\",\"uri\":\"spotify:artist:3ubFn9991d8ygM3MSi7NDi\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/1ozpmkWcCHwsQ4QTnxOOdT\"},\"href\":\"https://api.spotify.com/v1/albums/1ozpmkWcCHwsQ4QTnxOOdT\",\"id\":\"1ozpmkWcCHwsQ4QTnxOOdT\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/77b0c91524867cc72d1974f66ad8cd21d063a20e\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/f2405b82d0578dd815a3082ca0f7ec4e18e937a1\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/a5435bb3ab4fabe43bc7f7ce46a6c23aa30d8eae\",\"width\":64}],\"name\":\"What A Time To Be Alive\",\"type\":\"album\",\"uri\":\"spotify:album:1ozpmkWcCHwsQ4QTnxOOdT\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3ubFn9991d8ygM3MSi7NDi\"},\"href\":\"https://api.spotify.com/v1/artists/3ubFn9991d8ygM3MSi7NDi\",\"id\":\"3ubFn9991d8ygM3MSi7NDi\",\"name\":\"Future\",\"type\":\"artist\",\"uri\":\"spotify:artist:3ubFn9991d8ygM3MSi7NDi\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":205879,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51500300\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/27GmP9AWRs744SzKcpJsTZ\"},\"href\":\"https://api.spotify.com/v1/tracks/27GmP9AWRs744SzKcpJsTZ\",\"id\":\"27GmP9AWRs744SzKcpJsTZ\",\"name\":\"Jumpman\",\"popularity\":77,\"preview_url\":\"https://p.scdn.co/mp3-preview/4f3e954bb232a96c196389017d961016c8cbd7fc?cid=null\",\"track_number\":9,\"type\":\"track\",\"uri\":\"spotify:track:27GmP9AWRs744SzKcpJsTZ\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":267066,\"explicit\":false,\"external_ids\":{\"isrc\":\"USCM51500238\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/1OAYKfE0YdrN7C1yLWaLJo\"},\"href\":\"https://api.spotify.com/v1/tracks/1OAYKfE0YdrN7C1yLWaLJo\",\"id\":\"1OAYKfE0YdrN7C1yLWaLJo\",\"name\":\"Hotline Bling\",\"popularity\":75,\"preview_url\":\"https://p.scdn.co/mp3-preview/53a8f039eb0b567e47868f5a53de4683ba5d5f0c?cid=null\",\"track_number\":20,\"type\":\"track\",\"uri\":\"spotify:track:1OAYKfE0YdrN7C1yLWaLJo\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":189853,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600078\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/4YJmZfvlheSziXem8HBWrj\"},\"href\":\"https://api.spotify.com/v1/tracks/4YJmZfvlheSziXem8HBWrj\",\"id\":\"4YJmZfvlheSziXem8HBWrj\",\"name\":\"Still Here\",\"popularity\":73,\"preview_url\":\"https://p.scdn.co/mp3-preview/39384d3485d21184dd3719cfd8d644182b0b1d8b?cid=null\",\"track_number\":10,\"type\":\"track\",\"uri\":\"spotify:track:4YJmZfvlheSziXem8HBWrj\"},{\"album\":{\"album_type\":\"single\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/79qV4McLzhs8U3FyRKnocz\"},\"href\":\"https://api.spotify.com/v1/albums/79qV4McLzhs8U3FyRKnocz\",\"id\":\"79qV4McLzhs8U3FyRKnocz\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/2151a609fd5a5ec69586920a85bf308cdf56f3a1\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/9c6eb30ff5270c115b1ecd2b74430e505c281f25\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/ef4e90b4dde72134365a732659dccf9e1bd7b519\",\"width\":64}],\"name\":\"Back To Back\",\"type\":\"album\",\"uri\":\"spotify:album:79qV4McLzhs8U3FyRKnocz\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":170637,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51500241\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/5lFDtgWsjRJu8fPOAyJIAK\"},\"href\":\"https://api.spotify.com/v1/tracks/5lFDtgWsjRJu8fPOAyJIAK\",\"id\":\"5lFDtgWsjRJu8fPOAyJIAK\",\"name\":\"Back To Back\",\"popularity\":73,\"preview_url\":\"https://p.scdn.co/mp3-preview/b5bb11586af5cfde7c0eaef26300b2f6f62d2ac4?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:5lFDtgWsjRJu8fPOAyJIAK\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0ptlfJfwGTy0Yvrk14JK1I\"},\"href\":\"https://api.spotify.com/v1/albums/0ptlfJfwGTy0Yvrk14JK1I\",\"id\":\"0ptlfJfwGTy0Yvrk14JK1I\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/d329671363eb7826b5871eef978841c7db97c757\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/bcd6801c26cb293a45df9b092227395c5b403b4c\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/14d65d4565838431345e35575b8b74d95134990a\",\"width\":64}],\"name\":\"If You're Reading This It's Too Late\",\"type\":\"album\",\"uri\":\"spotify:album:0ptlfJfwGTy0Yvrk14JK1I\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":241853,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51500010\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/1ID1QFSNNxi0hiZCNcwjUC\"},\"href\":\"https://api.spotify.com/v1/tracks/1ID1QFSNNxi0hiZCNcwjUC\",\"id\":\"1ID1QFSNNxi0hiZCNcwjUC\",\"name\":\"Legend\",\"popularity\":72,\"preview_url\":\"https://p.scdn.co/mp3-preview/34fe00d7d951e42017bbbd8a424244c3cf1006e1?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:1ID1QFSNNxi0hiZCNcwjUC\"}]}")


print("1. How many songs are there?")

print("Tere are",len(data['tracks']),"songs in this dataset.")


print("2. List the name of each song, along with its popularity.")

num = 0

for track in data['tracks']:
    print(data['tracks'][num]['name'],"has a popularity of",data['tracks'][num]['popularity'])
    num = num + 1

print("3.How long would it take, in minutes, to listen to all of these songs in a row?")

num = 0
minutes_old = 0

for track in data['tracks']:
    ms = data['tracks'][num]['duration_ms']
    minutes_add = round(ms/60000,2)
    minutes_old = round(minutes_old + minutes_add,2)
print("To listenn to all of these songs in a row, it would take", minutes_old, "minutes")

print("4. For each song, list every artist that worked on it.")

n1 = 0

for track in data['tracks']:
    print("Song :", data['tracks'][n1]['name'])

    n2 = 0

    for artist in data['tracks'][n1]['artists']:
        print("Author : ", data['tracks'][n1]['artists'][n2]['name'])
        
        n2 = n2 + 1
   
    n1 = n1 + 1

print("5. For each song, list every musician that worked on it EXCEPT Drake")

n1 = 0

for track in data['tracks']:
    print("Song :", data['tracks'][n1]['name'])

    n2 = 0

    for artist in data['tracks'][n1]['artists']:
        if not data['tracks'][n1]['artists'][n2]['name'] == 'Drake':
            print("Author : ", data['tracks'][n1]['artists'][n2]['name'])
        
        n2 = n2 + 1
   
    n1 = n1 + 1

print("6. How many songs are from albums, and how many are from singles?")

n = 0
singles_n = 0
albums_n = 0

for track in data['tracks'][n]:
    if n < 10:
        if data['tracks'][n]['album']['album_type'] == 'single':
            singles_n = singles_n + 1
        elif data['tracks'][n]['album']['album_type'] == 'album':
            albums_n = albums_n + 1
    n = n + 1

print(f"There are {albums_n} songs from albums, and {singles_n} songs from singles.")

print("7. What percentage of these songs are marked as explicit?")

n = 0
explicit_true = 0
explicit_false = 0

for song in data['tracks']:
    lyrics = data['tracks'][n]['explicit']
    if lyrics == True:
         explicit_true = explicit_true + 1
    elif lyrics == False:
        explicit_false = explicit_false + 1

    n = n + 1

percentage = int(explicit_true/(explicit_true + explicit_false)*100)

print(f"The {percentage} percent of songs has explicit lyrics")

print("8. I'd like to listen to one of the songs! Is there maybe a URL where I can listen to it?")
import random

n = random.randint(0,9)

song_title = data['tracks'][n]['name']
song_url = data['tracks'][n]['preview_url']


print(f"You can listen to a preview of {song_title} by going to {song_url}")

print("9. What is the most popular song?")

n = 0
popularity = {}


for track in data['tracks'][n]:
    
    if n < 10:

        track_name = data['tracks'][n]['name']
        track_popularity = data['tracks'][n]['popularity']

        popularity[track_name] = track_popularity

        n = n + 1

pop_song_title = (max(popularity, key=popularity.get))        
pop_song_value = (max(popularity.values()))

print(f"The most popular song is {pop_song_title}, with a popularity score of {pop_song_value}.")

