import random
from operator import attrgetter

from deap import base
from deap import creator
from deap import tools

from trial import trial
from const import *

creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
#attr_uniform,
toolbox.register("attr_uniform", random.uniform, -2, 2)
toolbox.register("individual", tools.initRepeat, creator.Individual , toolbox.attr_uniform, \
                                INPUT_NUMBER*HIDDEN_LAYER_NUMBER + HIDDEN_LAYER_NUMBER*OUTPUT_NUMBER)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

#評価関数の作成
def evalOneMax(individual):
    return trial(individual),
toolbox.register("evaluate", evalOneMax)

#自前の突然変異関数
def myMutation(individual,indpb):
    for i in range(len(individual)):
        if random.random() < indpb:
            if random.random() < 0.75:
                individual[i] += random.uniform(-0.5,0.5)
                if individual[i] > 2.0:
                    individual[i] = 2.0
                elif individual[i] < -2.0:
                    individual[i] = -2.0
            else:
                individual[i] = 0.0
    return individual,

#交差、突然変異、選択用の関数
toolbox.register("mutate", myMutation, indpb=0.0035)
toolbox.register("select", tools.selTournament, tournsize=3)

def main():
    random.seed(64)
    # 初期の個体群を生成
    pop = toolbox.population(n=90)
    MUTPB, NGEN = 1.0, 10000 # 交差確率、突然変異確率、進化計算のループ回数

    print("Start of evolution")

    # 初期の個体群の評価
    fitnesses = list(map(toolbox.evaluate, pop))
    for ind, fit in zip(pop, fitnesses):
        ind.fitness.values = fit

    print("  Evaluated %i individuals" % len(pop))

    # 進化計算開始
    for g in range(NGEN):
        print("-- Generation %i --" % g)

        # 次世代の個体群を選択
        offspring = toolbox.select(pop, len(pop))
        # 個体群のクローンを生成
        offspring = list(map(toolbox.clone, offspring))
        # クローンを適応度順にソート(降順)
        offspring = sorted(offspring,key=attrgetter('fitness.values'),reverse=True)

        parent_pool = toolbox.select(offspring[0:40], len(offspring[0:40]))
        parent_pool= list(map(toolbox.clone, parent_pool))
        i = 0
        for mutant in parent_pool:
            toolbox.mutate(mutant)
            del mutant.fitness.values
            offspring[i+10] = mutant
            offspring[-i] = mutant
            i += 1


        # 適合度が計算されていない個体を集めて適合度を計算
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit


        print("  Evaluated %i individuals" % len(invalid_ind))

        # 次世代群をoffspringにする
        pop[:] = offspring

        # すべての個体の適合度を配列にする
        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        mean = sum(fits) / length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2 / length - mean**2)**0.5

        print("  Min %s" % min(fits))
        print("  Max %s" % max(fits))
        print("  Avg %s" % mean)
        print("  Std %s" % std)

    print("-- End of (successful) evolution --")

    best_ind = tools.selBest(pop, 1)[0]
    print("Best individual is %s, %s" % (best_ind, best_ind.fitness.values))

if __name__=='__main__':
    main()
