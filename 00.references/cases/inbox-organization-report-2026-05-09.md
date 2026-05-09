# inbox整理レポート（2026-05-09・修正版）

## 実施内容
- inbox内のPDF/Markdownを分類しました。
- PDFは重複候補を除き、originals/へ移動しました。
- PDF/Markdownから、markdown/raw/ と markdown/cleaned/ にMarkdownを生成しました。
- 各生成Markdownに frontmatter（case_id/title/source_pdf/theme/tags/status）を付与しました。
- 生成ファイル名の日付は、判決日・裁判年月日を優先して再確認しました。取得できない場合のみ date-unknown とする方針です。
- retio_no136-114.pdf 由来のMarkdownは、本文中の「名古屋地判 令5･12･14」から裁判年月日を再抽出し、2023-12-14 始まりのファイル名に修正しました。
- 現時点で date-unknown 始まりの生成ファイルは0件です。
- inboxに残っていたMarkdown 74件は、コピー生成済みのため inbox/archive-original-md/ に移動しました。削除はしていません。
- case-index.md は改変せず、追記候補一覧のみ維持しました。

## 移動ファイル一覧
### PDF
- `00.references/cases/inbox/retio_no135-106.pdf` -> `00.references/cases/originals/retio_no135-106.pdf`
- `00.references/cases/inbox/retio_no135-108.pdf` -> `00.references/cases/originals/retio_no135-108.pdf`
- `00.references/cases/inbox/retio_no135-110.pdf` -> `00.references/cases/originals/retio_no135-110.pdf`
- `00.references/cases/inbox/retio_no135-112.pdf` -> `00.references/cases/originals/retio_no135-112.pdf`
- `00.references/cases/inbox/retio_no135-114.pdf` -> `00.references/cases/originals/retio_no135-114.pdf`
- `00.references/cases/inbox/retio_no135-118.pdf` -> `00.references/cases/originals/retio_no135-118.pdf`
- `00.references/cases/inbox/retio_no136-114.pdf` -> `00.references/cases/originals/retio_no136-114.pdf`
- `00.references/cases/inbox/retio_no137-110.pdf` -> `00.references/cases/originals/retio_no137-110.pdf`
- `00.references/cases/inbox/retio_no137-114.pdf` -> `00.references/cases/originals/retio_no137-114.pdf`
- `00.references/cases/inbox/retio_no137-116.pdf` -> `00.references/cases/originals/retio_no137-116.pdf`
- `00.references/cases/inbox/retio_no137-118.pdf` -> `00.references/cases/originals/retio_no137-118.pdf`
- `00.references/cases/inbox/retio_no137-120.pdf` -> `00.references/cases/originals/retio_no137-120.pdf`
- `00.references/cases/inbox/retio_no137-132.pdf` -> `00.references/cases/originals/retio_no137-132.pdf`

### inbox Markdown
- `00.references/cases/inbox/archive-original-md/` にMarkdown 74件を移動済み

## 生成ファイル一覧
- raw: 88件 (`00.references/cases/markdown/raw/`)
- cleaned: 88件 (`00.references/cases/markdown/cleaned/`)
- 2026-05-09始まり: 0件
- date-unknown始まり: 0件

### cleaned
- `00.references/cases/markdown/cleaned/2002-11-15.baibai.悪臭被害を理由とした古民家の買主の宅建業者への損.md`
- `00.references/cases/markdown/cleaned/2018-03-17.baibai.RETIO.NO.1352024年秋号106賃借.md`
- `00.references/cases/markdown/cleaned/2018-12-15.baibai.RETIO.NO.1372025年春号114売買.md`
- `00.references/cases/markdown/cleaned/2020-01-17.baibai.協定内容に違反して車両を駐車させる等をした隣地所.md`
- `00.references/cases/markdown/cleaned/2020-01-30.baibai.売買契約締結後引渡前の買主による売買対象地の駐車.md`
- `00.references/cases/markdown/cleaned/2020-07-22.baibai.RETIO.NO.1352024年秋号108自動.md`
- `00.references/cases/markdown/cleaned/2020-10-13.chintai.賃貸人が雨漏り修繕等を怠ったとして退去した賃借人.md`
- `00.references/cases/markdown/cleaned/2021-01-14.baibai.買主が請求した土壌汚染対策工事費用に関して封じ込.md`
- `00.references/cases/markdown/cleaned/2021-02-08.baibai.RETIO.NO.1352024年秋号110融資.md`
- `00.references/cases/markdown/cleaned/2021-03-24.baibai.予定された借地契約を締結しなかった借主に対し、契.md`
- `00.references/cases/markdown/cleaned/2021-03-25.kanri.反復継続によるハトへの餌やりが、信頼関係の破壊に.md`
- `00.references/cases/markdown/cleaned/2021-04-05.baibai.隣家が2項道路セットバック部分の工作物等を撤去せ.md`
- `00.references/cases/markdown/cleaned/2021-06-16.baibai.媒介業者の説明・告知義務違反により開発事業を断念.md`
- `00.references/cases/markdown/cleaned/2021-07-30.chintai.引渡された建物の清掃が不充分であった等とする賃貸.md`
- `00.references/cases/markdown/cleaned/2021-08-25.baibai.再建築不可物件であるとの重要事項説明が正しくなさ.md`
- `00.references/cases/markdown/cleaned/2021-09-13.chintai.RETIO.NO.1372025年春号128賃貸.md`
- `00.references/cases/markdown/cleaned/2021-10-27.baibai.司法書士への登記書類の預け入れ等は履行の着手にあ.md`
- `00.references/cases/markdown/cleaned/2021-11-16.baibai.既存マンションの売買価格にリフォーム工事費用を含.md`
- `00.references/cases/markdown/cleaned/2021-11-29.baibai.土地買受検討先の売買取りやめについて媒介業者に債.md`
- `00.references/cases/markdown/cleaned/2021-11-30.baibai.RETIO.NO.1372025年春号132新築.md`
- `00.references/cases/markdown/cleaned/2021-11-30.baibai.雨漏りの補修を行う合意があったとして補修費用を求.md`
- `00.references/cases/markdown/cleaned/2021-12-10.baibai.RETIO.NO.1372025年春号118破産.md`
- `00.references/cases/markdown/cleaned/2021-12-15.baibai.特定緊急輸送道路沿道建築物の建物明渡請求について.md`
- `00.references/cases/markdown/cleaned/2021-12-24.baibai.契約における重要な要素についての双方の意思合致が.md`
- `00.references/cases/markdown/cleaned/2022-01-17.baibai.就職希望者へのマンション購入の勧誘について消費者.md`
- `00.references/cases/markdown/cleaned/2022-01-18.chintai.店舗の内装工事を不承認としたマンション管理組合と.md`
- `00.references/cases/markdown/cleaned/2022-01-19.kanri.2項道路のセットバック部分について、現実に道路が.md`
- `00.references/cases/markdown/cleaned/2022-01-20.chintai.障害者グループホームの利用が住宅以外の用途を禁じ.md`
- `00.references/cases/markdown/cleaned/2022-01-26.baibai.売買契約が確実に成立すると信頼を抱かせ、信義則上.md`
- `00.references/cases/markdown/cleaned/2022-01-28.baibai.投資マンションの実勢価格を調査説明しなかった営業.md`
- `00.references/cases/markdown/cleaned/2022-01-28.chintai.土地賃貸借に係る覚書締結後に契約締結を拒絶した土.md`
- `00.references/cases/markdown/cleaned/2022-02-24.baibai.瑕疵の対象範囲を制限する特約があるとして、責任対.md`
- `00.references/cases/markdown/cleaned/2022-02-28.baibai.リースバック取引に係る一連の行為が詐欺行為にあた.md`
- `00.references/cases/markdown/cleaned/2022-02-28.baibai.高齢者の買主が、違法な勧誘で別の原野を購入させら.md`
- `00.references/cases/markdown/cleaned/2022-03-02.baibai.無権代理を理由とした、売主の買主への請求が否認さ.md`
- `00.references/cases/markdown/cleaned/2022-03-02.chintai.賃借人の「彼女」が使者として賃貸借契約等を締結し.md`
- `00.references/cases/markdown/cleaned/2022-03-04.baibai.売主代理人の指示通りに買主が行った売買代金債務の.md`
- `00.references/cases/markdown/cleaned/2022-03-11.baibai.瑕疵担保免責特約に関して、その瑕疵に善意の売主の.md`
- `00.references/cases/markdown/cleaned/2022-03-11.chintai.豪雨による地下駐車場の浸水被害につき、過去の浸水.md`
- `00.references/cases/markdown/cleaned/2022-03-15.chintai.原状回復工事が実施されないがその費用を負担する旨.md`
- `00.references/cases/markdown/cleaned/2022-03-16.chintai.賃貸マンションの隣室居住者の喫煙により自宅保管商.md`
- `00.references/cases/markdown/cleaned/2022-03-22.baibai.土地を購入して賃貸する事業を提案した媒介業者に対.md`
- `00.references/cases/markdown/cleaned/2022-03-25.baibai.広告記載クラスの車両が入出庫できないとする、購入.md`
- `00.references/cases/markdown/cleaned/2022-03-29.baibai.タワーマンションの買主が建物の免震オイルダンパー.md`
- `00.references/cases/markdown/cleaned/2022-03-29.baibai.投資用物件の売主業者には、想定利回りに影響を及ぼ.md`
- `00.references/cases/markdown/cleaned/2022-03-29.baibai.賃貸マンションの機械式駐車場の劣化について売主・.md`
- `00.references/cases/markdown/cleaned/2022-03-29.baibai.隣地建物から落雪があったとして、その所有者や前所.md`
- `00.references/cases/markdown/cleaned/2022-04-28.baibai.手付解除が、手付解除期日か履行の着手いずれか遅い.md`
- `00.references/cases/markdown/cleaned/2022-04-28.chintai.賃貸マンション借主の迷惑行為による貸主の賃貸借契.md`
- `00.references/cases/markdown/cleaned/2022-05-25.baibai.売主業者がマンション隣室購入者の情報を正しく告げ.md`
- `00.references/cases/markdown/cleaned/2022-05-31.baibai.市街化調整区域の建物につき適法に居住できない旨の.md`
- `00.references/cases/markdown/cleaned/2022-06-16.baibai.コロナ禍の影響で購入原資を調達できなかった事情は.md`
- `00.references/cases/markdown/cleaned/2022-06-16.chintai.賃貸物件の賃料受領権限の付与に関する合意を共有者.md`
- `00.references/cases/markdown/cleaned/2022-06-20.baibai.売買契約が解除されても契約条項に基づく既払収益金.md`
- `00.references/cases/markdown/cleaned/2022-06-22.chintai.宅建業者が新規契約広告宣伝費名目で収受した媒介報.md`
- `00.references/cases/markdown/cleaned/2022-06-24.chintai.厨房の床がウェットキッチンでなかったとして賃貸借.md`
- `00.references/cases/markdown/cleaned/2022-06-24.chintai.小規模事務所の原状回復費用には国交省ガイドライン.md`
- `00.references/cases/markdown/cleaned/2022-07-19.baibai.売主の媒介業者代表者個人への預け金が、宅建業法6.md`
- `00.references/cases/markdown/cleaned/2022-09-13.baibai.売買契約成立を妨害されたとする媒介業者による媒介.md`
- `00.references/cases/markdown/cleaned/2022-09-15.baibai.営利法人の6件の転売取引に関与した買主側媒介業者.md`
- `00.references/cases/markdown/cleaned/2022-09-28.baibai.マンション管理費等の改定予定を知り得なかった売主.md`
- `00.references/cases/markdown/cleaned/2022-10-06.baibai.RETIO.NO.1352024年秋号114区分.md`
- `00.references/cases/markdown/cleaned/2022-10-14.chintai.耐震改修促進法の通行障害建築物内の店舗借主への立.md`
- `00.references/cases/markdown/cleaned/2022-10-14.chintai.賃借人の借室ベランダからの自殺事故による貸主の逸.md`
- `00.references/cases/markdown/cleaned/2022-10-27.baibai.RETIO.NO.1352024年秋号118投資.md`
- `00.references/cases/markdown/cleaned/2022-10-27.chintai.消防設備等に関し、建物が借主目的の民泊事業に使用.md`
- `00.references/cases/markdown/cleaned/2022-11-22.baibai.告知書に残置物「無」と記載した売主に不法行為責任.md`
- `00.references/cases/markdown/cleaned/2022-11-30.baibai.納戸を居室と表示した広告が不法行為または隠れた瑕.md`
- `00.references/cases/markdown/cleaned/2022-12-08.baibai.自己破産した買主代表の不法行為に対する売主の損害.md`
- `00.references/cases/markdown/cleaned/2022-12-15.baibai.民法213条の袋地が接する私道について、隣地使用.md`
- `00.references/cases/markdown/cleaned/2023-01-31.baibai.契約解除の意思表示には手付解除の黙示の意思表示が.md`
- `00.references/cases/markdown/cleaned/2023-02-14.baibai.私道についての一般車両が通行可能と買主に誤信させ.md`
- `00.references/cases/markdown/cleaned/2023-02-15.chintai.契約書面が無い建物使用貸借において貸主および借主.md`
- `00.references/cases/markdown/cleaned/2023-02-17.baibai.RETIO.NO.1352024年秋号112リフ.md`
- `00.references/cases/markdown/cleaned/2023-02-28.chintai.「然るべき金額の更新料を支払う」旨の特約には具体.md`
- `00.references/cases/markdown/cleaned/2023-03-15.baibai.RETIO.NO.1372025年春号110土地.md`
- `00.references/cases/markdown/cleaned/2023-03-16.baibai.媒介業者にローン解除権行使を妨害されたとする買主.md`
- `00.references/cases/markdown/cleaned/2023-03-16.baibai.実測清算の対象土地の範囲が明確でなかったため清算.md`
- `00.references/cases/markdown/cleaned/2023-03-30.baibai.更地渡しの内容に合意した売主が更地工事を行わない.md`
- `00.references/cases/markdown/cleaned/2023-05-25.baibai.RETIO.NO.1372025年春号120売買.md`
- `00.references/cases/markdown/cleaned/2023-05-25.baibai.引渡された改装済建物に建物売買価格を上回る補修費.md`
- `00.references/cases/markdown/cleaned/2023-05-25.baibai.特定空家の解体措置の代執行前に行なわれた、所有者.md`
- `00.references/cases/markdown/cleaned/2023-09-14.chintai.賃貸マンションの偶発的な転落死亡事故について、賃.md`
- `00.references/cases/markdown/cleaned/2023-10-25.baibai.ＬＰガス供給契約を解除した建売住宅の買主に対する.md`
- `00.references/cases/markdown/cleaned/2023-11-01.chintai.大規模修繕工事による騒音・臭気ならびにこれに伴う.md`
- `00.references/cases/markdown/cleaned/2023-11-27.chintai.賃借人は抵当権設定登記後に取得した賃貸人に対する.md`
- `00.references/cases/markdown/cleaned/2023-12-14.baibai.RETIO.NO.1362025年冬号114土地.md`
- `00.references/cases/markdown/cleaned/2024-03-28.baibai.RETIO.NO.1372025年春号116病院.md`

## 日付修正
- `2026-05-09.baibai.RETIO.NO.1362025年冬号114土地.md` -> `2023-12-14.baibai.RETIO.NO.1362025年冬号114土地.md`（裁判年月日: 2023-12-14）
- raw側・cleaned側の両方で `2023-12-14` 始まりのファイルを確認しました。
- raw側・cleaned側の両方で `date-unknown` 始まりのファイルは確認されませんでした。

## case-index.md 追記候補
- `candidate-retio130-2` / source: `retio130-2.md` / theme: 騒音 / title: 悪臭被害を理由とした古民家の買主の宅建業者への損害賠償請求について悪臭の発生が認められる証拠はないとして棄却された事例
- `candidate-retio_no135-106` / source: `retio_no135-106.pdf` / theme: 管理実務 / title: RETIO.   NO.135 2024   年秋号 106 賃借中の不動産の買受け交渉中に他者に売 却されてしまったために他者からの買い戻し に過分な支出を余
- `candidate-retio_no137-114` / source: `retio_no137-114.pdf` / theme: 売買 / title: RETIO.   NO.137 2025   年春号 114 売買契約成立後、買主の債務不履行により 契約解除となり、売主が媒介業者に対する媒 介報酬の支払を拒
- `candidate-retio130-13` / source: `retio130-13.md` / theme: 告知義務 / title: 協定内容に違反して車両を駐車させる等をした隣地所有者に対する通行権確認・通行妨害禁止の請求が認容された事例
- `candidate-retio134-3` / source: `retio134-3.md` / theme: 原状回復 / title: 売買契約締結後引渡前の買主による売買対象地の駐車場として使用方法が違約にあたるとする売主の主張が認められなかった事例
- `candidate-retio_no135-108` / source: `retio_no135-108.pdf` / theme: 売買 / title: RETIO.   NO.135 2024   年秋号 108 自動消滅型融資特約のある売買契約につ き、解除期日経過後の覚書によって売買代金 支払時期が延長され
- `candidate-retio131-10` / source: `retio131-10.md` / theme: 契約解除 / title: 賃貸人が雨漏り修繕等を怠ったとして退去した賃借人の連帯保証人に対する賃貸人の未払い賃料等の請求が一部認容された事例
- `candidate-retio133-5` / source: `retio133-5.md` / theme: 売買 / title: 買主が請求した土壌汚染対策工事費用に関して封じ込め工事費用の請求のみ認め、掘削除去工事費用の請求は棄却された事例
- `candidate-retio_no135-110` / source: `retio_no135-110.pdf` / theme: 告知義務 / title: RETIO.   NO.135 2024   年秋号 110 融資利用特約期限経過後に、取引建物の適 合証明書の発行が受けられず、予定していた フラット35に適
- `candidate-retio132-8` / source: `retio132-8.md` / theme: 管理実務 / title: 予定された借地契約を締結しなかった借主に対し、契約締結上の過失があるとして、貸主に対する損害金の支払いが認容された事例
- `candidate-retio130-9` / source: `retio130-9.md` / theme: 騒音 / title: 反復継続によるハトへの餌やりが、信頼関係の破壊にあたるとして無催告での賃貸借契約解除が認められた事例
- `candidate-retio133-13` / source: `retio133-13.md` / theme: 管理実務 / title: 隣家が2項道路セットバック部分の工作物等を撤去せず、所有不動産の適正な価格での売却が阻害されたとする訴えが棄却された事例
- `candidate-retio131-7` / source: `retio131-7.md` / theme: 告知義務 / title: 媒介業者の説明・告知義務違反により開発事業を断念したとする買主業者の損害賠償請求が棄却された事例
- `candidate-retio130-11` / source: `retio130-11.md` / theme: 原状回復 / title: 引渡された建物の清掃が不充分であった等とする賃貸マンションの賃借人による賃貸人に対する損害賠償等の請求が棄却された事例
- `candidate-retio132-3` / source: `retio132-3.md` / theme: 告知義務 / title: 再建築不可物件であるとの重要事項説明が正しくなされているとして、買主による契約無効や損害賠償等の請求が棄却された事例
- `candidate-retio131-2` / source: `retio131-2.md` / theme: 売買 / title: 司法書士への登記書類の預け入れ等は履行の着手にあたらないとして決済日前日の買主の手付解除を認めた事例
- `candidate-retio133-4` / source: `retio133-4.md` / theme: 告知義務 / title: 既存マンションの売買価格にリフォーム工事費用を含める合意があったとする買主の主張が棄却された事例
- `candidate-retio134-8` / source: `retio134-8.md` / theme: 告知義務 / title: 土地買受検討先の売買取りやめについて媒介業者に債務不履行・注意義務違反があったとする売主の損害賠償請求が棄却された事例
- `candidate-retio_no137-132` / source: `retio_no137-132.pdf` / theme: 告知義務 / title: RETIO.   NO.137 2025   年春号 132 新築賃貸マンションの敷地内に設置された ゴミ置場について、その向かい側の住民が、 設置の説明がなか
- `candidate-retio131-5` / source: `retio131-5.md` / theme: 告知義務 / title: 雨漏りの補修を行う合意があったとして補修費用を求めたが、すべて解決していたとして却下された事例
- `candidate-retio_no137-118` / source: `retio_no137-118.pdf` / theme: 管理実務 / title: RETIO.   NO.137 2025   年春号 118 破産した売主業者による高額な賃貸物件の 転売に共謀又は幇助があったとして、買主が 融資銀行に対して
- `candidate-retio131-13` / source: `retio131-13.md` / theme: 管理実務 / title: 特定緊急輸送道路沿道建築物の建物明渡請求について、立退料の支払いをもって正当事由が認められた事例
- `candidate-retio132-6` / source: `retio132-6.md` / theme: 管理実務 / title: 契約における重要な要素についての双方の意思合致がされていないとして、黙示の媒介契約の成立が否定された事例
- `candidate-retio136-6` / source: `retio136-6.md` / theme: 告知義務 / title: 就職希望者へのマンション購入の勧誘について消費者契約法第4条の困惑により契約取消しが認められた事例
- `candidate-retio130-8` / source: `retio130-8.md` / theme: 管理実務 / title: 店舗の内装工事を不承認としたマンション管理組合と貸主に対する、借主の損害賠償請求が棄却された事例
- `candidate-retio130-12` / source: `retio130-12.md` / theme: 管理実務 / title: 2項道路のセットバック部分について、現実に道路が開設された状態になったとは認められないと判断された事例
- `candidate-retio133-12` / source: `retio133-12.md` / theme: 管理実務 / title: 障害者グループホームの利用が住宅以外の用途を禁じる管理規約に反し、区分所有者の共同の利益に反する行為にあたるとされた事例
- `candidate-retio134-1` / source: `retio134-1.md` / theme: 売買 / title: 売買契約が確実に成立すると信頼を抱かせ、信義則上の義務違反があるとした主張が否定された事例
- `candidate-retio130-4` / source: `retio130-4.md` / theme: 告知義務 / title: 投資マンションの実勢価格を調査説明しなかった営業担当者に対する買主の損害賠償請求が認容された事例
- `candidate-retio136-7` / source: `retio136-7.md` / theme: 管理実務 / title: 土地賃貸借に係る覚書締結後に契約締結を拒絶した土地所有者に対する賃借予定者による支払済み設計料等の請求が認容された事例
- `candidate-retio131-4` / source: `retio131-4.md` / theme: 売買 / title: 瑕疵の対象範囲を制限する特約があるとして、責任対象外の建物傾斜等に係る損害賠償請求を棄却した事例
- `candidate-retio130-5` / source: `retio130-5.md` / theme: 管理実務 / title: リースバック取引に係る一連の行為が詐欺行為にあたるとして転売利益相当額が損害賠償額として認められた事例
- `candidate-retio132-7` / source: `retio132-7.md` / theme: 原状回復 / title: 高齢者の買主が、違法な勧誘で別の原野を購入させられ、所有権移転登記抹消と損害賠償を請求をし、認められた事例
- `candidate-retio136-3` / source: `retio136-3.md` / theme: 売買 / title: 無権代理を理由とした、売主の買主への請求が否認された事例
- `candidate-retio133-9` / source: `retio133-9.md` / theme: 管理実務 / title: 賃借人の「彼女」が使者として賃貸借契約等を締結したとする保証会社の主張が棄却された事例
- `candidate-retio130-1` / source: `retio130-1.md` / theme: 売買 / title: 売主代理人の指示通りに買主が行った売買代金債務の弁済は、民法478条の効力があるとして、売主に所有権移転登記手続を命じた事例
- `candidate-retio132-2` / source: `retio132-2.md` / theme: 売買 / title: 瑕疵担保免責特約に関して、その瑕疵に善意の売主の責任は否定され、悪意の売主の責任が認められた事例
- `candidate-retio131-11` / source: `retio131-11.md` / theme: 管理実務 / title: 豪雨による地下駐車場の浸水被害につき、過去の浸水に対する対応を行っていた貸主の責任は認められなかった事例
- `candidate-retio131-9` / source: `retio131-9.md` / theme: 原状回復 / title: 原状回復工事が実施されないがその費用を負担する旨の合意について借主の動機の錯誤が認められた事例
- `candidate-retio134-11` / source: `retio134-11.md` / theme: 管理実務 / title: 賃貸マンションの隣室居住者の喫煙により自宅保管商材等に損害が生じたとする借主の請求が棄却された事例
- `candidate-retio132-9` / source: `retio132-9.md` / theme: 管理実務 / title: 土地を購入して賃貸する事業を提案した媒介業者に対して地代支払開始日について誤った説明をしたことによる賠償責任が認められた事例
- `candidate-retio130-3` / source: `retio130-3.md` / theme: 告知義務 / title: 広告記載クラスの車両が入出庫できないとする、購入6年後に買主が訴えた損害賠償請求が棄却された事例
- `candidate-retio132-1` / source: `retio132-1.md` / theme: 売買 / title: タワーマンションの買主が建物の免震オイルダンパーに建築基準法違反の疑い等があるとして錯誤無効を求めたが棄却された事例
- `candidate-retio132-5` / source: `retio132-5.md` / theme: 管理実務 / title: 投資用物件の売主業者には、想定利回りに影響を及ぼし得る法令上の制限を調査説明する義務があるとした事例
- `candidate-retio131-6` / source: `retio131-6.md` / theme: 告知義務 / title: 賃貸マンションの機械式駐車場の劣化について売主・媒介業者が説明義務を怠ったとする買主の主張が棄却された事例
- `candidate-retio132-12` / source: `retio132-12.md` / theme: 管理実務 / title: 隣地建物から落雪があったとして、その所有者や前所有者に落雪防止のための屋根の改築等を求めたが棄却された事例
- `candidate-retio131-1` / source: `retio131-1.md` / theme: 告知義務 / title: 手付解除が、手付解除期日か履行の着手いずれか遅い時期まで可能な契約であったとする売主主張が棄却された事例
- `candidate-retio130-10` / source: `retio130-10.md` / theme: 騒音 / title: 賃貸マンション借主の迷惑行為による貸主の賃貸借契約の解除及び解除後の使用料相当損害金等の賠償請求が認められた事例
- `candidate-retio131-8` / source: `retio131-8.md` / theme: 騒音 / title: 売主業者がマンション隣室購入者の情報を正しく告げないことは債務不履行等に当たるとした買主の主張が棄却された事例
- `candidate-retio136-4` / source: `retio136-4.md` / theme: 告知義務 / title: 市街化調整区域の建物につき適法に居住できない旨の説明をしなかった媒介業者に対する慰謝料等が認められた事例
- `candidate-retio133-2` / source: `retio133-2.md` / theme: 売買 / title: コロナ禍の影響で購入原資を調達できなかった事情は買主の責めに帰すことができない事由とはいえないとした事例
- `candidate-retio132-10` / source: `retio132-10.md` / theme: 管理実務 / title: 賃貸物件の賃料受領権限の付与に関する合意を共有者が自己に有利な内容に変更することは認められないとした事例
- `candidate-retio133-3` / source: `retio133-3.md` / theme: 原状回復 / title: 売買契約が解除されても契約条項に基づく既払収益金の返還がされないことが合意されていたと認められた事例
- `candidate-retio131-12` / source: `retio131-12.md` / theme: 管理実務 / title: 宅建業者が新規契約広告宣伝費名目で収受した媒介報酬の報酬制限超過部分や架空費用等の返還を認めた事例
- `candidate-retio133-8` / source: `retio133-8.md` / theme: 管理実務 / title: 厨房の床がウェットキッチンでなかったとして賃貸借契約の錯誤無効を主張した借主の請求が棄却された事例
- `candidate-retio133-11` / source: `retio133-11.md` / theme: 原状回復 / title: 小規模事務所の原状回復費用には国交省ガイドライン等の適用があるとの賃借人の主張が否認された事例
- `candidate-retio134-9` / source: `retio134-9.md` / theme: 売買 / title: 売主の媒介業者代表者個人への預け金が、宅建業法64条の8の取引により生じた債権に該当しないとされた事例
- `candidate-retio133-7` / source: `retio133-7.md` / theme: 売買 / title: 売買契約成立を妨害されたとする媒介業者による媒介報酬相当額の損害賠償請求が棄却された事例
- `candidate-retio130-6` / source: `retio130-6.md` / theme: 売買 / title: 営利法人の6件の転売取引に関与した買主側媒介業者代表者に無免許営業幇助を認定し罰金刑を言い渡した事例
- `candidate-retio133-6` / source: `retio133-6.md` / theme: 告知義務 / title: マンション管理費等の改定予定を知り得なかった売主及び媒介業者の買主への説明義務違反を否定した事例
- `candidate-retio_no135-114` / source: `retio_no135-114.pdf` / theme: 告知義務 / title: RETIO.   NO.135 2024   年秋号 114 区分所有建物の買主業者が、共用部分であ る外壁に専有部分への雨漏りの原因となる亀 裂があった、また
- `candidate-retio136-9` / source: `retio136-9.md` / theme: 管理実務 / title: 耐震改修促進法の通行障害建築物内の店舗借主への立退料300万円以内の貸主申出について900万円は下らないとして棄却された事例
- `candidate-retio134-10` / source: `retio134-10.md` / theme: 管理実務 / title: 賃借人の借室ベランダからの自殺事故による貸主の逸失利益について賃料の11.7か月分を認めた事例
- `candidate-retio_no135-118` / source: `retio_no135-118.pdf` / theme: 管理実務 / title: RETIO.   NO.135 2024   年秋号 118 投資マンション ３ 物件を380万円で購入し、 3,600万円で売却した売主業者及び勧誘者に、 買
- `candidate-retio130-7` / source: `retio130-7.md` / theme: 管理実務 / title: 消防設備等に関し、建物が借主目的の民泊事業に使用できるかの調査は借主自身が行う必要があるとされた事例
- `candidate-retio134-6` / source: `retio134-6.md` / theme: 告知義務 / title: 告知書に残置物「無」と記載した売主に不法行為責任があるとした主張が棄却された事例
- `candidate-retio136-5` / source: `retio136-5.md` / theme: 告知義務 / title: 納戸を居室と表示した広告が不法行為または隠れた瑕疵にあたるとした売主業者への損害賠償請求が棄却された事例
- `candidate-retio131-3` / source: `retio131-3.md` / theme: 売買 / title: 自己破産した買主代表の不法行為に対する売主の損害賠償請求権は破産法の非免責債権に該当するとして、売主の訴えを認容した事例
- `candidate-retio132-11` / source: `retio132-11.md` / theme: 売買 / title: 民法213条の袋地が接する私道について、隣地使用権による工事車両の通行は認められ通行権は否定された事例
- `candidate-retio133-1` / source: `retio133-1.md` / theme: 売買 / title: 契約解除の意思表示には手付解除の黙示の意思表示が含まれていたと認められた事例
- `candidate-retio132-4` / source: `retio132-4.md` / theme: 告知義務 / title: 私道についての一般車両が通行可能と買主に誤信させた媒介業者及びその担当者に損害賠償責任を認めた事例
- `candidate-retio136-10` / source: `retio136-10.md` / theme: 管理実務 / title: 契約書面が無い建物使用貸借において貸主および借主間に使用貸借期間の合意があったとして建物明渡請求が認められた事例
- `candidate-retio_no135-112` / source: `retio_no135-112.pdf` / theme: 告知義務 / title: RETIO.   NO.135 2024   年秋号 112 リフォーム転売された築20年の中古マンシ ョンの引渡し１か月後に発生した地下室の漏 水について、隠
- `candidate-retio136-11` / source: `retio136-11.md` / theme: 管理実務 / title: 「然るべき金額の更新料を支払う」旨の特約には具体的権利性を認めることはできないとして更新料請求を棄却した事例
- `candidate-retio_no137-110` / source: `retio_no137-110.pdf` / theme: 告知義務 / title: RETIO.   NO.137 2025   年春号 110 土地建物を購入した買主が、売主と近隣住 民との間に告知されていないトラブルがあ り、これは契約不適
- `candidate-retio134-7` / source: `retio134-7.md` / theme: 告知義務 / title: 媒介業者にローン解除権行使を妨害されたとする買主の訴えが棄却された事例
- `candidate-retio134-4` / source: `retio134-4.md` / theme: 告知義務 / title: 実測清算の対象土地の範囲が明確でなかったため清算条項の解釈で争いとなり、売主・買主の認識に基づき判断された事例
- `candidate-retio136-2` / source: `retio136-2.md` / theme: 売買 / title: 更地渡しの内容に合意した売主が更地工事を行わないため、買主がその工事を実施して費用等の支払を求め、認められた事例
- `candidate-retio_no137-120` / source: `retio_no137-120.pdf` / theme: 売買 / title: RETIO.   NO.137 2025   年春号 120 売買契約書において土地の代金額と建物の代 金額とが明示的に区分されていたとしても、 消費税法施行令
- `candidate-retio134-5` / source: `retio134-5.md` / theme: 契約解除 / title: 引渡された改装済建物に建物売買価格を上回る補修費用を要する瑕疵があったことにより買主の契約解除が認められた事例
- `candidate-retio134-2` / source: `retio134-2.md` / theme: 売買 / title: 特定空家の解体措置の代執行前に行なわれた、所有者と第三者との売買契約が通謀虚偽表示により無効とされた事例
- `candidate-retio133-10` / source: `retio133-10.md` / theme: 管理実務 / title: 賃貸マンションの偶発的な転落死亡事故について、賃借人が心理的瑕疵を貸室に発生させたとはいえないとした事例
- `candidate-retio134-12` / source: `retio134-12.md` / theme: 売買 / title: ＬＰガス供給契約を解除した建売住宅の買主に対する供給会社による設備残存価格の支払い請求が認められた事例
- `candidate-retio136-8` / source: `retio136-8.md` / theme: 騒音 / title: 大規模修繕工事による騒音・臭気ならびにこれに伴う健康被害が発生したとする賃借人の請求が棄却された事例
- `candidate-retio136-12` / source: `retio136-12.md` / theme: 管理実務 / title: 賃借人は抵当権設定登記後に取得した賃貸人に対する債権との相殺合意を抵当権者に対抗できないとされた事例
- `candidate-retio_no136-114` / source: `retio_no136-114.pdf` / theme: 売買 / title: RETIO.   NO.136 2025   年冬号 114 土地及び建物の売買契約を締結したとこ ろ、売主が、約定の期日までに、契約の条件 である本件土地の確
- `candidate-retio_no137-116` / source: `retio_no137-116.pdf` / theme: 売買 / title: RETIO.   NO.137 2025   年春号 116 病院建築用地の取得にあたり、買主法人が 業務委託先の宅建業者に支払った業務委託費 について、買主法

## 重複候補
- `00.references/cases/inbox/retio_no137-128.pdf`: 同名PDFが `00.references/cases/originals/retio_no137-128.pdf` に存在します。方針どおり削除せず、保留として inbox に残しています。

## 未整理候補
- `retio_no137-128.pdf`

## 確認結果
- raw: 88件
- cleaned: 88件
- inbox/archive-original-md: 74件
- 2026-05-09始まりの生成ファイル: 0件
- date-unknown始まりの生成ファイル: 0件
- retio_no136-114.pdf由来の2023-12-14ファイル: 2件（raw/cleaned各1件）
- inboxに残っている通常ファイル: retio_no137-128.pdf
- case-index.md: 変更なし

## エラー
- なし
