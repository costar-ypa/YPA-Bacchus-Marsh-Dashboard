from pathlib import Path

path = Path('index.html')
text = path.read_text(encoding='utf-8')
marker = '/* FINAL PHOTO CACHE FIX */'
if marker in text:
    raise SystemExit('Final photo fix already present')

override = r'''

    /* FINAL PHOTO CACHE FIX */
let ypaPhotoIndexPromise = null;
let ypaPhotoIndex = null;

getLocalPhotos = async function(h){
    const folder = photoFolder(h).trim().toLowerCase();

    try{
        if(!ypaPhotoIndex){
            if(!ypaPhotoIndexPromise){
                ypaPhotoIndexPromise = (async () => {
                    const response = await fetch(
                        "https://api.github.com/repos/costar-ypa/YPA-Bacchus-Marsh-Dashboard/git/trees/main?recursive=1",
                        { cache:"no-store" }
                    );

                    if(!response.ok){
                        throw new Error(`GitHub tree request failed: ${response.status}`);
                    }

                    const data = await response.json();
                    const index = new Map();

                    (data.tree || []).forEach(file => {
                        if(!file || file.type !== "blob" || !file.path) return;

                        const parts = String(file.path).split("/");
                        if(parts.length < 3 || parts[0].toLowerCase() !== "images") return;

                        const filename = parts[parts.length - 1];
                        if(!/\.(jpg|jpeg|png|webp|gif|avif)$/i.test(filename)) return;

                        const folderKey = parts[1].trim().toLowerCase();
                        if(!index.has(folderKey)) index.set(folderKey, []);

                        const encodedPath = parts
                            .map(segment => encodeURIComponent(segment))
                            .join("/");

                        index.get(folderKey).push(
                            `${GITHUB_PAGES_BASE}/${encodedPath}`
                        );
                    });

                    for(const photos of index.values()){
                        photos.sort((a,b) =>
                            a.localeCompare(b, undefined, {
                                numeric:true,
                                sensitivity:"base"
                            })
                        );
                    }

                    return index;
                })();
            }

            ypaPhotoIndex = await ypaPhotoIndexPromise;
            ypaPhotoIndexPromise = null;
        }

        return ypaPhotoIndex.get(folder) || [];

    }catch(error){
        console.error("Photo loading error:", error);
        ypaPhotoIndexPromise = null;
        return [];
    }
};
'''

needle = '\n</script>\n\n</body>'
if needle not in text:
    raise SystemExit('Could not locate closing script/body')

text = text.replace(needle, override + needle, 1)
path.write_text(text, encoding='utf-8')
