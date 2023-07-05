using System.Collections.Generic;

public class FrequencyTracker
{
    private Dictionary<int, int> map;
    private Dictionary<int, int> frequencies;

    public FrequencyTracker()
    {
        map = new Dictionary<int, int>();
        frequencies = new Dictionary<int, int>();
    }

    public void Add(int number)
    {
        if (map.ContainsKey(number))
        {
            int prevFrequency = map[number];
            map[number]++;
            UpdateFrequency(prevFrequency, prevFrequency + 1);
        }
        else
        {
            map[number] = 1;
            UpdateFrequency(0, 1);
        }
    }

    public void DeleteOne(int number)
    {
        if (map.ContainsKey(number))
        {
            int prevFrequency = map[number];
            map[number]--;
            UpdateFrequency(prevFrequency, prevFrequency - 1);
            if (map[number] <= 0)
            {
                map.Remove(number);
            }
        }
    }

    public bool HasFrequency(int frequency)
    {
        return frequencies.ContainsKey(frequency);
    }

    private void UpdateFrequency(int oldFrequency, int newFrequency)
    {
        if (oldFrequency > 0)
        {
            frequencies[oldFrequency]--;
            if (frequencies[oldFrequency] <= 0)
            {
                frequencies.Remove(oldFrequency);
            }
        }

        if (newFrequency > 0)
        {
            if (frequencies.ContainsKey(newFrequency))
            {
                frequencies[newFrequency]++;
            }
            else
            {
                frequencies[newFrequency] = 1;
            }
        }
    }
}
