module FastAlgorithm 

    export bifurcation

    function bifurcation(time_range, x_start, p_range, f, up_border=10_000, down_border=1e-5)
        values = Dict()

        for p ∈ p_range
            values[p] = []

            x_0 = x_start
            for _ ∈ time_range
                x_t = f(p, x_0)
                if (up_border ≠ Nothing) && (abs(x_t) > up_border)
                    break
                end
                if (down_border ≠ Nothing) && (abs(x_t) < down_border)
                    break
                end 
                x_0 = x_t
            end
            for _ ∈ time_range
                x_t = f(p, x_0)
                if (up_border ≠ Nothing) && (abs(x_t) > up_border)
                    break
                end
                if (down_border ≠ Nothing) && (abs(x_t) < down_border)
                    break
                end 
                x_0 = x_t

                push!(values[p], x_t)
            end
        end

        return values
    end
end