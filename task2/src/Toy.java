package src;

/** Сущность игрушки */
public class Toy {
    /** Идентификатор игрушки */
    private long id;

    /** Название игрушки */
    private String title;

    /** Частота выпадения игрушки. Должна быть от 1 до 100 */
    private float weight;

    /**
     * Инициализация игрушки.
     * @param id Идентификатор игрушки.
     * @param title Название игрушки.
     * @param weight Частота выпадения игрушки. Должна быть от 1 до 100.
     */
    public Toy(long id, String title, float weight) {
        validateWeight(weight);

        this.id = id;
        this.title = title;
        this.weight = weight;
    }

    /**
     * Обновить частоту выпадения игрушки. Должна быть от 1 до 100.
     * @param weight Новая частота выпадения.
     */
    public void setWeight(float weight) {
        validateWeight(weight);
        this.weight = weight;
    }

    /** Получить идентификатор игрушки */
    public long getId() {
        return id;
    }

    /** Получить название игрушки */
    public String getTitle() {
        return title;
    }

    /** получить частоту выпадения игрушки */
    public float getWeight() {
        return weight;
    }

    @Override
    public String toString() {
        return String.format("[%s] %s", id, title);
    }

    /**
     * Проверить корректность частоты выпадения игрушки.
     * @param weight Частота выпадения игрушки.
     * @throws RuntimeException при некорректном значении.
     */
    private void validateWeight(float weight) {
        //проверим корректность частоты
        if (weight < 1 || weight > 100) {
            throw new RuntimeException("Некорректная частота игрушки");
        }
    }
}