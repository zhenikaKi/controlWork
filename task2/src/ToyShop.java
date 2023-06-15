package src;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.PriorityQueue;
import java.util.stream.Collectors;

/** Магазин игрушек */
public class ToyShop {
    /** Список всех игрушек. В качестве ключа выступает игрушка, а в значении - количество игрушек в магазине */
    private Map<Toy, Integer> toys = new LinkedHashMap<>();

    private PriorityQueue<Toy> priorityQueue;

    /** Инициализация списка с игрушками */
    public ToyShop() {
        try {
            //открываем файл
            File file = new File("task2/data.txt");
            BufferedReader bufferedReader = new BufferedReader(new FileReader(file));
            while (bufferedReader.ready()) {
                String line = bufferedReader.readLine();
                parseLine(line, toys);
            }
            bufferedReader.close();

            //формируем очередь из игрушек
            priorityQueue = new PriorityQueue<>(toys.size(), Comparator.comparingDouble(Toy::getWeight));
            priorityQueue.addAll(toys.keySet());
        }
        catch (Exception e) {
            throw new RuntimeException("Возникла ошибка при инициализации магазина", e);
        }
    }

    /**
     * Изменить вес игрушки по ее идентификатору.
     * @param id Идентификатор игрушки.
     * @param weight Новый вес игрушки.
     */
    public void changeWeight(int id, float weight) {
        toys.keySet().forEach(t -> {
            if (t.getId() == id) {
                t.setWeight(weight);
            }
        });
        priorityQueue.clear();
        priorityQueue.addAll(
                toys.entrySet().stream()
                        .filter(e -> e.getValue() > 0)
                        .map(Entry::getKey)
                        .collect(Collectors.toList()));
    }

    /** Получить данные по всем игрушкам */
    public List<ToyInfo> getToysInfo() {
        return toys.entrySet().stream()
                .map(t -> new ToyInfo(t.getKey(), t.getValue()))
                .collect(Collectors.toList());
    }

    /**
     * Добавить игрушку.
     * @param id Идентификатор игрушки.
     * @param title Название игрушки.
     * @param weight Частота выпадения игрушки. Должна быть от 1 до 100.
     * @param count Оставшееся количество игрушек в магазине
     */
    public void addToy(long id, String title, float weight, int count) {
        Toy toy = new Toy(id, title, weight);
        toys.put(toy, count);
        priorityQueue.add(toy);
    }

    /** Получить игрушки из очереди игрушек */
    public Toy getToy() {
        boolean correct = false;
        Toy toy;
        do {
            toy = priorityQueue.poll();
            if (toy == null) {
                continue;
            }

            //проверяем, есть ли еще запасы по игрушке в магазине
            int count = toys.getOrDefault(toy, 0);
            count--;
            toys.put(toy, count);

            //взяли не последнюю игрушку
            if (count >= 0) {
                //обновляем количество игрушек в магазине
                correct = true;
                if (count > 0) {
                    priorityQueue.add(toy); //игрушку помещаем обратно в очередь, т.к. по ней еще есть запасы
                }
            }
        } while (!correct && toy != null);

        return toy;
    }

    /**
     * Распарсить строку с данными по игрушке.
     * @param line Строка с данными по игрушке.
     * @param toys Ранее сформированный список игрушек.
     */
    private void parseLine(String line, Map<Toy, Integer> toys) {
        String[] data = line.split(";");
        Toy toy = new Toy(Integer.parseInt(data[0]), data[1], Float.parseFloat(data[2]));
        toys.put(toy, Integer.parseInt(data[3]));
    }
}
