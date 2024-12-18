from curses.ascii import isalnum
import re
DATA = [
    ".854...........................................................................362...........271...732........838.........24................",
    "...*.............................117*...........459........767*648....#.........*...................................$...&..=................",
    "....970.........368.124.+............57................653...........723.....366....*443..60.........536....441....45..879.....789...*......",
    "...........749*...-...+..330.....................215%...*................725.....953........%.................*............639......331.419.",
    ".......706.....59.............*....=...262.............678...........857.*............189....................912.+589.846*...*..............",
    "..........*................393.59..418....*................151...........594...........*....584*258.......................17.997............",
    ".......774....275........................777........841..............988.........121....908.........86.....482..295....................@....",
    ".110..........%.....605..@.......305*18...............*....740.............840..*................52*.......*...........100...........250....",
    "...........*..............856..............412.........761....*....344....*.....505.....................121......709...-....-...............",
    "......980.269..189+............701..............22...$........343..*...684..............-375......223........97.*..........890......443.....",
    "..904*..................555.....*.......38.....*....207............773.......................824.....*.......*..../....618..................",
    "....................355*........362....*......442.$..........613...........%770.......526.....*.......418.....283..76....*....862...........",
    "...450....*292..............735.....149...........143..........*...458...........279.........43..769...................$..48.....*..........",
    "....*..413.........983*....*.................679.......642....214...#........107*......=.........*.....%...........276.39......196.889*624..",
    "...128.................658.515...890#...................../...........................60..../....528..359.....451...*.....56................",
    "...................719...................525.................$502............284-........@...489.................#..287.....@....+..........",
    "...849...............*................../.........................282.+649...............217............240.....................833.....930.",
    ".......666...179.....986.526................./927......73.....176*...............@...459...........=946..*..488...126.....*.................",
    "..........@.....*549.....@...261.....370*951...........+.............114......170.......@...............269............471.891.$859.........",
    ".............................../.................646.....-.327........*..237..............452......../......*620..713...............324.....",
    "..................=716.....753....................-....431..=.......692.%.......210.......*.......860....208...............81*655....$......",
    "......298....17*..........+....................................................*..........603................950.218.$......................",
    "................692...54......+778.809........140..*.........249............%.332..............*.........372*......*.328.....=..............",
    ".......421.............#..............+........*....493.......*..........589..................286...............254..........458...672...258",
    "........*.....949.630.....725...609.........408.............108..............304.517......829.........666*..........724.182...........*.=...",
    ".........435./....*..........*.*................580..................@.........*..&..147.-......221*......544..662/....*...........881......",
    "..750.............561......568.487.@...935.......*....106...........104......808.......*............333...................&900..............",
    "...................................287.$......930.....&.....*528.........332............755..................840../.............583.....209.",
    ".371.299.................503.............................632................*.......&...................500........647..193.......-.........",
    "....*........-902..2.123..*...912.......775......./...............241........734....90.968.513..66.566...................*..&...............",
    "..................*....@.923...*.......*.....289..47.....785..710.......54................*......*....................767....452....=....597",
    ".............348.362............607.....889.....#........*....*........*......$904................694...............................241.....",
    "....955........*.....559*792............................307..25.........449..............*751.404.....134.....841...........................",
    "......&.959...300............446.504.644....692...............................#.................-.....*.......*...758*35....................",
    ".908$...*...........&..861...........=.....%....240............-..+..9.514...615.....&....-646.....538...144.751...........899.........545..",
    ".......806.270*....946.@...............*..........*.555@....803..322.-............410..........514.................510..10..*.....858..-....",
    "...............373....................7.918.....699.........................710.......&...........-.....78%............+....34..............",
    "....653...............................................553.......896.......-......&...721....970.............................................",
    ".......%...........379..377.....770@.................$.....126....*...712.287....951.........*......984*..........+.............+700........",
    "..............924...*....*.............422...................*...233.*........................124...........902....181......................",
    "................&....156..363.....*855....*.................884......509..879..755.......$...........*635......*........283.........661.....",
    "..559..........................393.........766...789.............683..................461..#......910.........904.........$.%......*.....13.",
    ".........=...568.........680/.......................*......*522.#..........................747...........*113................702...952......",
    "....*....334...*...392..........910*...............233..189.........219.879............225......521...941...................................",
    ".146.981......284.*.......*972......391.....789*...................................628*.....*....*................675.......................",
    "..................921..151......................983...............582......983.690.......213.137.268.............*..............24$.........",
    "....561....................600........106-...............226..................*.....996.............................681.....768.......852...",
    "..............................%............................$................=...963..$.....@............421*305.......*.....*........$......",
    ".....923.285*.....961...........*......$812......812..851.............678.29.......*......501.....228..............385...853...........251..",
    ".444*...............*...998...99.711.............+.....*......330.....*.........287...........781..+..........%445..........................",
    "......$....250=.....965...*.............................113...$......766....$.......941........-......658.............894........351........",
    "......335...............463.328*.....411....%.............................981.113......*5.............*...773=.573&....*............$.......",
    "..........%348..................460.....*5..517.......583.261.....889@.......................953.....496...............547............620...",
    "...299.................367.......................+....*................852.442.796.........*.@...............=................834.....*.....",
    "....*....772...487.......................#......938.462.956..41.643...*.....#.....*592....66...809.368..3..549........................772...",
    ".566........*.....*320.....498..775.230.193....................*......961.........................*....*.......%283.....406.......495.......",
    "........292..585..............*.*.....*..........213...*309...................469..549......413........903................*....29..*........",
    ".........*.......@.........551..806...489......................51.655.999*.......*.$.............21*.................300..931....*..595.....",
    "......878......62../...........................871......169..=..&..*......235..788...497..........................68....*.......191.........",
    ".144.........+.....31............-...............*..623*....428.....955...............*.............424....89....*......728.............*665",
    ".............447...............530...203...955.336..........................227........665.......$.........*.....669..............473.......",
    "835...................*323..............*./...........=.....24..........*.........................452.......9.............263.........570...",
    "......568...803@.....................152.......209.933.....*....877..667.895............548...963......................................*....",
    ".......$.........=............................*...........948..-...................171.*........*.605.765..-........90..............992.....",
    "..360..........#.476...........................564../.............755*...............+..709...11.....*......909..........696..124%..........",
    "........74...73................320.........658......739...=...........484...860*....................................314.....................",
    "...=509...*.........79.290........*...222...*.............46...940..............960.....473.....320..........$681......*591..269....../.....",
    "........887.94@......*..*.........302...+.784.554+............+......#......455........./............891..........457........*...609.120....",
    "....................874.246.....................................+.....228..*....&.........272....%..$.....*377.....*..52..604....%..........",
    ".....44.....870*457................905.45......58...............956.........935.551...807..$.....21....356.......317....................%...",
    ".........=...................267......*...300=.........543..............398..............#.................$.......................386...745",
    "..........145......+............................*......*...........7....$.............64...........646....675..1..930..770.....791.$........",
    "................744....462......443&......*389..575..965...805....+..14.......761*578..-...#..776...*..................-........-.......822.",
    "....668.484...............*............875.................*.........*....................227...*..908.............215......*.......270.....",
    ".......*......771..........318....883......881...........655.@26..130..799.......876..91......28...........699.........807...510............",
    ".............-........391*.........*.......+......903..................*.....379.*....@...........713........#............*.................",
    "..........+................196..230...........411....*965..682.......873....$.....916....755....&..=.....................296......+958.983..",
    "...*.....718.......279........%...............................*.271.............@.......*......932.......621..637.843..................*....",
    "..59..........%2...........................................400...*...142.870...746......256..........865*...........%...=.....%...409...761.",
    "............@...........122*157...........394........%.444.....207...-......*.........................................434..827...*..........",
    ".....266..19.....=..............624.......*........398....*................373...........418...16.....654.878*.................890..........",
    "...............487..........884....*......199.227........723......914*411...........228..........%...................872................-...",
    ".....937..608.................*....306........$....................................*..................522..309.@16.....*.............765....",
    "......#....................128../.................%136....140.................773...114...........33....*....*.........615.....303..........",
    ".249.....590..$...949..768.......380......%...996..............833...28...310.#...................*..338.....770...559......................",
    "...+.854.../.678..*....................646...*.........................=...&..............#.....422...................#.231...714.122.......",
    "......*...........552........................741..........+.......437........455*768..134..69..........*........519.......*........*........",
    ".......976.............466......497$.............607......783........*....*.............@..............28........-.........279......394.....",
    "............%....857...*....542.........915.543..$...............979...581.66......555....................331...................281.........",
    "....715......542..#..20....@........241...*...*.........701.......$...........113...../...193..96*305........&................/...#...489...",
    "219*...................................#.599...845.....*.....................$....*.........*...................$....996...240........*.....",
    "..........151.520...554.............................665..........................1.398.=450..426.....198.....326.....+..........-....129....",
    ".........*...........*.................687..............588....62..........504................................................970...........",
    "..........463.....776......804............*..............*.....*..........%....90/...834.790...514...740.770.......667......................",
    "....392..................................371...184........906.56....575.............*.............*.........*......*......435.....308.......",
    "....*..........*......908..........497...........................-.........884....849............374.....620....727......&........../.......",
    ".125........862.326......&........+..........497.....&811.......213.......*...........465....................64.....993.....................",
    "......................%.....288...............*...-.......617...........-..677........*.....32..........-907.+........*.....=....48.475.....",
    ".........787.........400.....*.......420....884.425......*.....420...727........#27..181.....*....414..............986......114./.....#..404",
    "........*.......%...........596....=.*....................863................$................428..*......899.....................114.......",
    ".595=.112.737.699................382.888..........................315...@...325..........480........115..*.........-......368...............",
    "...........*......+.@......652.*...............................&.....@..182.......219$.........945+.............844...........996....744*...",
    "..87......749..535...395..#....339..564.....813....410.........135...........330.......828...........585......................*..........870",
    "...+........................$........+..967*.........*....921......321......%................612@....*......................44..............",
    ".......764...716............818..327..............578.......*...../...........941..................736..@421........762.........282.........",
    "861#......*..@.......982..........*.........+...............714.................*..867.....863........................@....614....=.........",
    "........549................*....260.........91................................85.....$........*.803*895..622.$..............*.........684...",
    "............770*346.....714.652......145.........270...286..........#.......................66..........*.....337.176.813...483...223*......",
    "..........................................*..392..&.........505...957.@.........158...285......881#....497.........+...*....................",
    ".........=../..../.....588........227....639............741*..........443..681..........+..153........................335...................",
    "........201.671.96......$............*.....................................*........415.......*........-.......155...........848.58&........",
    "............................922......92...........180..........................&39...%....208..389......696.....*............=.......883.852",
    "....237.........950.........*............80..............................................*....................657.......................*...",
    "....../..611.......*.....671...443...971.&....366....381...442....458...$.......589.343.397.....463.......60.......&........125......&......",
    "..853...../..945..564...........*......*.......@......-................783..........*.......................*.......28......=.........373...",
    "................*.......+843..550..998.973.........+.....208.565..@..............231......292............+.365..172............+............",
    "......117......615..................*............299............&..862.895............/86...*....114..552........*...697.....733...388......",
    ".....................................212..261........885...............*...903..26*..........50.....-..........158................*.........",
    "...../........11..360....748......................67....*272.....320...16.....*....137.905......239......470......................433.......",
    "...141........*.....%......+......967........-...%...........243...*.......904............*....*..............88.377......619...............",
    "................=.....-668....%.....=.+461..525.....662.....*......196..28..............778...940..400..682...*...*.........*..638*.........",
    "779#..113........209...........744....................*...144..811....../...#......................-...*.....297..713.....50................",
    ".........$................#.........844...6...........62.......*.............957...&.......112@.......211.............173....989............",
    "..749.......$......989..931................*....&............424.........709.......867............590...................*.......*..645......",
    "...*..290...573......*............437....227.....53......132............#....471%.............501..%..................733.....270.....=.....",
    "..637...*............596............................=....*.......400...............*...........*....................................#.......",
    "......958.....757%.........=.........228......624...746.81../.....*........../..718.198..38...184..............*820..774......./830.693.....",
    ".........................453...405.=...=....................100.144.......728...........*...................498............$................",
    "..616............................*.756...310.........#52.............130.......=........506.....509.779..........723.......182..+...........",
    "...*....49.....-..............551..........*................789./.....*......306...613........./......*..491....*...............791..931....",
    "...863.....%.72......832.653........*490....814.....984.....=...741...568..........*.................998........567........+........#.......",
    ".........171..........*..-.......406...............*....389.....................486.....630............../...............457.576............",
    "..............308..515..................373@......709..&..............*185..................689..........751........44..........*764........",
    "..............*..............661....=.........*.............993....984.....*.......908......=...273............../.*........................",
    ".......582..335...260....59......998../.....39.760.313*174...*..........@.183......................*47....&994.887.577........*464.....22...",
    "......*...............................449..................802........762.....522..139+..154..266$......................46.323.....712*.....",
    "....827.....................................35......600*29.....724........488............*...............149*227.........*..................",
    "........@......278*............@..135..........594.........470*...........*....540*.......42..............................775.536..790......",
    ".....990...........742......181....*..............*..@521................743.......552............310...*....+738.....................*.....",
    ".......................125.......311............715........263...........................................173...................235....291...",
]

def check_row(row_num:int, start_index:int, end_index:int, row_position:str) -> bool:
    global DATA
    found_symbol = False
    row_to_check:str
    if row_position == "up":
        row_to_check = DATA[row_num+1]
    else:
        row_to_check = DATA[row_num-1]

    for ind, char in enumerate(row_to_check[::]):
        if ind in range(start_index-1, end_index+1):
            if not char.isalnum() and char != '.':
                found_symbol = True
                break
    return found_symbol

def main():
    global DATA
    good_nums:list[int] = []
    for row_num, row_str in enumerate(DATA):
        for num in re.finditer(r"\d+", row_str):
            found_symbol = False

            if row_num != 0: found_symbol = check_row(row_num, num.start(), num.end(), "down")
            if found_symbol:
                good_nums.append(int(num.group()))
                continue

            if row_num != len(DATA)-1: found_symbol = check_row(row_num, num.start(), num.end(), "up")
            if found_symbol:
                good_nums.append(int(num.group()))
                continue

            if not row_str[num.start()-1].isalnum() and row_str[num.start()-1] != ".":
                good_nums.append(int(num.group()))
                continue

            if num.end() != len(row_str):
                if not row_str[num.end()].isalnum() and row_str[num.end()] != ".":
                    good_nums.append(int(num.group()))
                    continue


    print(sum(good_nums))

if __name__ == "__main__":main()