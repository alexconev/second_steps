**Условие:**

Великата Стена разделяла Острова на Програмистите на две части - едната била на програмистите пишещи на **Pascal**, другата - на пишещите на **C**. Това било направено с цел срещите им да се сведат до нула понеже иначе се стигало до спорове, завършващи в Пирогов. Стената була тухлена, като тухлите били наредени в колони, плтно залепени една до друга и с еднаква височина. Но една нощ вандали (програмисти на асемблер) разместили тухлите, като вземали от една колона и ги слагали върху някоя друга. Така стената станала неравна и можело да се мине през нея. Това било недопустимо, затова бил извикан известния майстор - Quick Basic, който трябвало да възстанови стената. Но Quick Basic имал странен нрав - искал, преди да започне работа всичко да е предефинирано и известно, затова сега му е необходимо да научи с колко премествания на тухли може да се свърши работата и ако може с по-малко защото и не е е много паметлив. На Вас се пада задачата да откриете (независимо от коя страна на стената сте) какъв е минималния брой тухли, които трябва да се преместят за да се изравни стената, като напишете програма **WALL*. Под едно преместване се разбира: вземаме **p** тухли от една колона с поне **p** тухли ( броя на тухлите в тази колона намалява с **p**) и ги слагаме върху някоя друга колона ( броя на тухлите във втората колона се увеличава с **p**). На първия ред на стандартния вход е зададено цялото число **N**, 1 <= N <= 3000, показващо броя на колоните в стената. На следващия ред, със списък от цели положителни числа е описана самата стена, като на i-то място в списъка се намира цяло число **Xi**, 0 <= **Xi** <= 60000, показващо броя на тухлите в i-тата колона. Общият брой на тухлите в стената не надвишава 60000. На екрана програмата трябва да изведе намерния минамален брой премествания.

**Вход #1:**
	
	4
	10 8 12 18

**Изход #1:**

	2
